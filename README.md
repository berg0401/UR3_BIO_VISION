# UR5 BIO VISION 
## Introduction 
This project was developed by an intern at Université de Sherbrooke to equip a UR5 collaborative robot with vision capabilities. The robot performs biological experiments and interacts with its environment similarly to a human, simplifying the gradual automation of university manipulations. It utilizes an Intel RealSense D415 camera (available at Intel RealSense D415) to capture images. With an integrated visual component, the robot fulfills three main objectives:

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




