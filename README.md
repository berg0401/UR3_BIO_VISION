# UR3 BIO VISION 
## Introduction 
This project was developed by an intern at Université de Sherbrooke to equip a UR3 collaborative robot with vision capabilities. The robot performs biological experiments and interacts with its environment similarly to a human, simplifying the gradual automation of university manipulations. It utilizes an Intel RealSense D415 camera (available at Intel RealSense D415) to capture images. With an integrated visual component, the robot fulfills three main objectives:

Measure Agar: Determine the height of the gelatinous substance in a petri dish, onto which liquid is dispensed to observe bacterial growth.

Monitor Thermo-cycler State: Verify the operational status of the thermo-cycler that the robot interacts with.

Validate Thermo-cycler Inputs: Confirm that the robot has correctly entered the desired volume on the thermo-cycler's interface.

## First Mandate : Measure the Agar
Agar is a gelatinous substance housed in a petri dish. Its height is crucial for accurately placing a liquid drop on its surface. Penetration into the substance is limited to 1 mm, ensuring the liquid touches the surface due to insufficient gravitational force.

![image](https://github.com/user-attachments/assets/38a13972-4aff-47c5-a880-240bdbb4fcb7)
![image](https://github.com/user-attachments/assets/8b9cffc1-c88d-49f4-a73a-65201d8a1840)

Due to its transparency, a laser cannot be used. Instead, the height is measured in 2D using the camera with images such as: 
![02_Color](https://github.com/user-attachments/assets/f3fc2345-9824-4a15-b59f-a3eac00a7763)

Image processing involves cropping, applying an HSV filter using the OpenCV library, and subsequently applying a median filter to isolate the agar. The red color channel is retained, as it yielded optimal results with our LED strip:
![1](https://github.com/user-attachments/assets/66e0e830-c629-47bc-9b0d-919d3d83e3c6)

Contours are identified using the find contours function to detect rectangles and determine their height: 
![1](https://github.com/user-attachments/assets/98ea9e5f-c3cf-415e-9150-2b81e63f4e4e)

Using the agar's height in pixels, along with the camera's focal length, pixel size on the sensor, and the distance from the petri dish to the camera, the theorem of similar triangles is applied to calculate the agar's height in millimeters: 
![image](https://github.com/user-attachments/assets/a32d2000-4d1f-4632-879e-24bdc8946d52)


The complete pipeline is located in the petry_height_evaluator directory:
![image](https://github.com/user-attachments/assets/0514e946-ee79-4963-a3ab-62319d3ac08c)

For ideal results with the virtual aperture, it is recommended to take a 1280x720 pixel picture. If you change the picture's resolution, change the crop and the virtual aperture values accordingly. They are now ideal with a 1280x720 pixel image.

You must put the robot's joints in this configuration to have the right agar relative position to the camera and apply the theorem of similar triangles:

![image](https://github.com/user-attachments/assets/df5eec7c-8405-4cfc-a026-937516794b50)


## Second Mandate : Monitor Thermo-Cycler's State
The robot presses on the Thermo-Cycler's touch screen with a custom pen to interact with it. To confirm that the contact has been made and that the thermo-cycler is in the right state, the robot's camera captures an image of the screen like this:
![18_Color](https://github.com/user-attachments/assets/948b85c2-63f7-411d-8958-28924dbecbc4)

There are 23 screen states that are relevant for the robot protocols: 10 "pop ups" and 13 menus. The "pop ups" can technically appear from any menu.
"Pop ups": 
![09_Color](https://github.com/user-attachments/assets/366c30f4-5b91-4582-8e5a-02e54562b334)

Menus:
![01_Color](https://github.com/user-attachments/assets/c8bd3f15-a46f-4c48-a352-b1033764b88d)

To recognize different "pop ups" and menus of the thermo-cycler, we use Google's OCR as an API. It reads the different labels on the screen. In the code, some labels are called "features." To be considered a menu's feature, it needs to be exclusive to this menu and allow the algorithm to identify the menu by its presence alone. The feature is defined by the word it spells and its location on the screen.

In the previous images, you can see white spots. These are caused by the room's light bulbs. Because of them, each menu and "pop up" needs features at multiple locations on the screen to ensure that the state is recognized even if a white spot covers a feature. In this picture, the features of the "Saved Protocols" menu are circled in red:
![image](https://github.com/user-attachments/assets/48b01e2b-5d79-4481-9da8-b6bb319755b8)

The light bulb's effect on the image is reduced by adjusting the camera's settings like this (exposure and gain very low):
![image](https://github.com/user-attachments/assets/4ddd4864-b02d-4b05-a432-ca2a3b8c3a31)

To process the image, the algorithm follows these steps:
1. Crops the image.
2. Detects and reads labels.
3. Compares the labels to the features of each screen.
4. Determines the menu that owns a feature matching a label's word and location.

The confirm_thermo_state/thermo_state_initializer.py file contains the ThermoStateInitializer class. This class initializes each menu and their features for comparison with the labels read by the camera. It's important to initialize the "pop ups" before the menus because some of them don't occupy the entire screen. You can still see menu features while a "pop up" is displayed. For example, the "Confirm Protocol" "pop up" on the "Saved Protocols" menu allows for recognition of exclusive menu features:
![07_Color](https://github.com/user-attachments/assets/36ec808c-873d-4dd8-9165-61e3df494490)

By initializing them first, their features are analyzed first by the algorithm. If no labels match the features of the "pop up," we can conclude that it is indeed a menu. It's therefore mandatory to maintain this order when initializing the menus:
![image](https://github.com/user-attachments/assets/757981f3-bd53-4488-9af7-ee3ecd901138)

To take a picture and read it's content, you must run /confirm_thermo_state/main.py. This code will take one picture and adjsut the camera's settings with the RealsenseCamera object, crop the image with ImageEncoder, and read the text with textReader: 

![image](https://github.com/user-attachments/assets/bedcd068-4e7a-493a-95ff-0202dc023dcf)

The robot must be in this position:


![2eede12c-e630-4fb2-b05b-6d156681a3e5](https://github.com/user-attachments/assets/67d59a41-67d7-439d-969a-a02e02fc1d4b)

The thermo cycler must be at this position : 


![image](https://github.com/user-attachments/assets/5d7248ca-8cba-486c-9e7f-36fcaeae59ca)

It's possible to read pre-captured image from the /state_menu_demo_images directory. The confirm_thermo_state/text_reader.py's main function uses the imageFetcher object to get the images from the files, imageEncoder to crop the image and read the text with the textReader object: 


![image](https://github.com/user-attachments/assets/10e5f8f5-91ad-4659-af7c-cecf9fdea66a)





You must build your own json authentification key with Google OCR to use the algorithm and paste it in your cloned repo. 

## Third Mandate : Confirm Thermo-Cycler's Input

Sometimes, the thermo-cycler doesn’t detect the pen touching its screen. The robot must confirm that the correct button was pressed. To achieve this, a picture is taken of the area where the keyboard’s input is displayed. Using Google OCR’s API, we verify that the result matches the intended input.

Since the keyboard’s input is always displayed in the same area of the screen, the algorithm cannot gather features from all around the image, as it needs to avoid interference from the room’s light bulbs on the screen. If a white spot appears in the keyboard’s display section like this (worst case):
![01_Color](https://github.com/user-attachments/assets/b03116d7-88cb-4e52-824b-402c2822c033)
it becomes impossible to confirm the input.

The solution is to adjust the camera settings to eliminate the white spot from the screen:
![01_Color](https://github.com/user-attachments/assets/9fb7094a-e533-4fc5-b7c6-5f0484a28e9c)
Settings :

![ebec2a36-584b-4c1b-b439-eb04383a35c7](https://github.com/user-attachments/assets/890de580-0084-4ffd-befe-7aa78a72071d)

However, these settings degrade the image quality. To enhance the image quality, three pictures are taken and superimposed. The result looks like this : 
![image](https://github.com/user-attachments/assets/a4ec9c2e-b1b6-474f-9945-33b6462ff1d1)

Google OCR API's sends a list called texts. The first element is all the words on the screen. The second element is the first word and the third is the second word. We take only the second element, which is the number without it's units. In the picture above, it would be "20". 

To take a picture and read it's content, you must run /confirm_thermo_input/main.py. This code will take 3 pictures and adjsut the camera's settings with the RealsenseCamera object, crop and rotate the image with ImageEncoder, and read the text with textReader: 


![image](https://github.com/user-attachments/assets/fb531de8-2c0a-4509-88d7-96fc588496d6)

To have an accurate result, the robot must be placed at this position:


![image](https://github.com/user-attachments/assets/572dc027-8cdc-442a-a800-3fd067dd5f9e)



The thermocycler must be at this position: 


![image](https://github.com/user-attachments/assets/5d7248ca-8cba-486c-9e7f-36fcaeae59ca)

It's possible to read pre-captured image from the /input_thermo_demo_images directory. The confirm_thermo_input/text_reader.py's main function uses the imageFetcher object to get the images from the files, imageEncoder to crop and rotate the image and read the text with the textReader object: 


![image](https://github.com/user-attachments/assets/10e5f8f5-91ad-4659-af7c-cecf9fdea66a)



















