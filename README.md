# UR5 BIO VISION 
## Introduction 
This project was created by an intern at Université de Sherbrooke. It provides vision to a UR5 collaborative robot. The robot conducts biological experiences and interact with his environnement the same way a human does, to simplify the gradual automatisation of the university's manipulations. It uses a Intel realsense 415 camera (https://store.intelrealsense.com/buy-intel-realsense-depth-camera-d415.html) to catpure images. With a visual component inside the arm, it can now accomplish three mandates. The first one is to measure the agar, on wich liquid is poured to visualize growth of bacteries. The second one is to confirm the state of the thermo-cycler that the robot interacts with. The last one is to confirm that the robot has written the right volume on the thermo-cycler's keyboard. 

## First Mandate : measure the Agarw
The agar is and gelatinous substance stored in a petri pot. We need its height to pour a drop of liquid on it's surface. We can penetrate to a mamximum of 1 mm inside the substance. The liquide drop must touch the surface because the gravity is not strong enough to make it fall on it. 
![image](https://github.com/user-attachments/assets/38a13972-4aff-47c5-a880-240bdbb4fcb7)
![image](https://github.com/user-attachments/assets/8b9cffc1-c88d-49f4-a73a-65201d8a1840)

Since it's transparent, we can't use a laser. We then must measure the height in 2D with the camera with a picture like this : 
![02_Color](https://github.com/user-attachments/assets/f3fc2345-9824-4a15-b59f-a3eac00a7763)

We crop the image, do a HSV filter with the opencv library, than a median filter to isolate the agar. We only keep the red color of the image, since it's the color that showed the best results with our LED strip.
![1](https://github.com/user-attachments/assets/66e0e830-c629-47bc-9b0d-919d3d83e3c6)

We than use the find contours function to detect rectangles and we get it's height. 
![1](https://github.com/user-attachments/assets/98ea9e5f-c3cf-415e-9150-2b81e63f4e4e)

By knowing the agar's height in pixels, the focal length of the camera, the size of a pixel on the sensor and the distance of the petri pot from the camera, we can use the theorem of similar triangles to find the height of the agar in millimeters. 
![image](https://github.com/user-attachments/assets/a32d2000-4d1f-4632-879e-24bdc8946d52)


The pipeline is in the petry_height_evaluator directory. 
![image](https://github.com/user-attachments/assets/0514e946-ee79-4963-a3ab-62319d3ac08c)




