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


## Second Mandate: Monitor Thermo-Cycler's State
The robot interacts with the Thermo-Cycler’s touch screen using a custom pen. To confirm that the contact has been made and the Thermo-Cycler is in the correct state, the robot’s camera captures an image of the screen.

### Screen States
There are 23 relevant screen states for the robot protocols: 10 "pop-ups" and 13 menus. "Pop-ups" can appear from any menu.

Pop-ups: 
![09_Color](https://github.com/user-attachments/assets/366c30f4-5b91-4582-8e5a-02e54562b334)

Menus: 
![01_Color](https://github.com/user-attachments/assets/c8bd3f15-a46f-4c48-a352-b1033764b88d)

Recognizing "Pop-ups" and Menus
Google’s OCR API reads the labels on the screen to identify different "pop-ups" and menus. Labels are referred to as "features" in the code. A feature is considered part of a menu if it is unique to that menu and helps in identifying it. Features are defined by the text they spell and their location on the screen.

Example of Features: The features of the "Saved Protocols" menu are circled in red: 
![image](https://github.com/user-attachments/assets/48b01e2b-5d79-4481-9da8-b6bb319755b8)

The effect of light bulbs on the image can be reduced by adjusting the camera’s settings (with very low exposure and gain): 
![image](https://github.com/user-attachments/assets/4ddd4864-b02d-4b05-a432-ca2a3b8c3a31)

### Image Processing Steps
Crop the image.
Detect and read labels.
Compare the labels to the features of each screen.
Determine the menu by matching features based on label text and location.
The confirm_thermo_state/thermo_state_initializer.py file contains the ThermoStateInitializer class, which initializes each menu and their features for comparison with the labels read by the camera. It’s crucial to initialize "pop-ups" before menus because some "pop-ups" do not cover the entire screen, allowing the algorithm to still detect menu features. For instance, the "Confirm Protocol" pop-up on the "Saved Protocols" menu allows recognition of exclusive menu features: ![07_Color](https://github.com/user-attachments/assets/36ec808c-873d-4dd8-9165-61e3df494490)

By initializing "pop-ups" first, their features are analyzed before menu features. If no labels match "pop-up" features, the algorithm concludes that it is a menu. It is mandatory to maintain this initialization order:
![image](https://github.com/user-attachments/assets/757981f3-bd53-4488-9af7-ee3ecd901138)

Some menus have identical labels because they imply the same reaction from the robot. For example, the edit protocol and new protocol menus are both labeled "edit protocol," and warning pop-ups are labeled "warning pop-up" regardless of their specific content.

### Running the Code
To capture and read an image, run /confirm_thermo_state/main.py. This script will:

Capture one image and adjust the camera’s settings using the RealsenseCamera object.
Crop the image using ImageEncoder.
Read the text with TextReader.

![image](https://github.com/user-attachments/assets/bedcd068-4e7a-493a-95ff-0202dc023dcf)

### Robot and Thermo-Cycler Positioning
Robot Position: 
![2eede12c-e630-4fb2-b05b-6d156681a3e5](https://github.com/user-attachments/assets/67d59a41-67d7-439d-969a-a02e02fc1d4b)

Thermo-Cycler Position: 
![image](https://github.com/user-attachments/assets/5d7248ca-8cba-486c-9e7f-36fcaeae59ca)

Pre-captured images can be found in the /state_menu_demo_images directory. The confirm_thermo_state/text_reader.py file’s main function uses the ImageFetcher object to get images from files, ImageEncoder to crop the image, and TextReader to read the text.

![image](https://github.com/user-attachments/assets/10e5f8f5-91ad-4659-af7c-cecf9fdea66a)

You must build your own JSON authentication key for Google OCR and paste it into your cloned repository.

## Third Mandate: Confirm Thermo-Cycler's Input
Sometimes, the Thermo-Cycler may not detect the pen touch on its screen. To verify that the correct button was pressed, a picture is taken of the area where the keyboard’s input is displayed. Google OCR’s API verifies that the result matches the intended input.

### Handling White Spots
If a white spot appears in the keyboard’s display section: ![01_Color](https://github.com/user-attachments/assets/b03116d7-88cb-4e52-824b-402c2822c033), it may hinder input confirmation.

### Solution
Adjust the camera settings to reduce the white spot effect: 
![01_Color](https://github.com/user-attachments/assets/9fb7094a-e533-4fc5-b7c6-5f0484a28e9c)
Settings: 
![ebec2a36-584b-4c1b-b439-eb04383a35c7](https://github.com/user-attachments/assets/890de580-0084-4ffd-befe-7aa78a72071d)

However, these settings may degrade image quality. To improve quality, take three pictures and superimpose them. The result should look like this: 
![image](https://github.com/user-attachments/assets/a4ec9c2e-b1b6-474f-9945-33b6462ff1d1)

The Google OCR API returns a list called texts. The first element contains all words on the screen. The second element is the first word, and the third is the second word. Use the second element, which represents the number without units. For example, the picture above would show "20".

### Running the Code
To capture and read an image, run /confirm_thermo_input/main.py. This script will:

Capture three images and adjust the camera’s settings using the RealsenseCamera object.
Crop and rotate the images using ImageEncoder.
Read the text using TextReader.

![image](https://github.com/user-attachments/assets/fb531de8-2c0a-4509-88d7-96fc588496d6)

### Accurate Positioning
Robot Position: 
![image](https://github.com/user-attachments/assets/572dc027-8cdc-442a-a800-3fd067dd5f9e)

Thermo-Cycler Position: 
![image](https://github.com/user-attachments/assets/5d7248ca-8cba-486c-9e7f-36fcaeae59ca)

Pre-captured images can be found in the /input_thermo_demo_images directory. The confirm_thermo_input/text_reader.py file’s main function uses the ImageFetcher object to get images from files, ImageEncoder to crop and rotate the image, and TextReader to read the text.

![image](https://github.com/user-attachments/assets/10e5f8f5-91ad-4659-af7c-cecf9fdea66a)
