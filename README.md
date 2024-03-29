# Image Quality Estimators for Frames
As to the continuation of the prior project https://github.com/ambparth/yolov5datlab.git, the next step is to quantify the frames or the images. This is because the volume of data is high and not all of this data is necessary for us. Therefore in order to so, the images or the frames are first quantified on the basis of similarity, noise and the change in the surrounding or addition of a newer object into the surrounding. 

## FR-IQA (Full Reference- Image Quality Assessment)
In majority cases of quantising images, a particular image is compared with another image which is usually considered as the reference or the ground truth. FR-IQA exploits this approach outputs a score. This score depends on the method that is used.

### Structural Similarity Index (SSIM)
The structural Similarity Index compares the similarity of the two images based on Features points and outputs a score in the range of 0-100. Higher the score indicates that the images are similar to one another.

### Mean Squared Error (MSE)
The mean squared error is one of the common metrics almost in every fields. This finds the error between the two images and squares it. The error ranges from zero to an infinite value, where more the value, indicate higher change in surrounding.

### Peak Signal to Noise Ratio (PSNR)
The peak signal to noise ratio gives information of the quality too, with higher value indicating more information and lesser value indicating that there is noise in the system. This method is infact not a very popular one these days as it does the analysis neither in the patch level nor in the feature level but more importantly in the pixel level. 

## NR-IQA (No Reference- Image Quality Assessment)
The FR-IQA gives a good estimate of the image, but the estimate is done mainly by checking the similarity of the images, which in practical case will not ply as, for istance it will be meaningless to say that blured image is somwhat similar to that of the original image. The other practical aspect to think about is the reference or Ground Truth. Like as discussed in the above paragraph, the ambiguity of ground truth presides. So therefore each and every frame has to be scored. 

### BRISQUE
This No-reference quality metric scores the image based on know distortions. Higher the score, lower the quality of image. 

### NIQE
This metric is trained purely on clean images, yet has the ability to quantify the image. Lower the score higher the quality. 

### PIQUE
This metric on the other hand is inspired by the human perception of image assessment. Lower the score, higher is the quality. 

## CODE LAYOUT

Firstly, before running the code, it is to be made sure that the python libraries are in place. Run the following code for it. 
>pip install -r requirements.txt

Run this code for analysing the FR-IQA metrics on the frames. The metrics are also saved as text files for a future analysis. 
>python fr_iqa.py

Similarly for the NR-IQA methods, the functions are taken from https://github.com/guptapraful/niqe.git and https://github.com/buyizhiyou/NRVQA.git with some minor tweakings. The metrics are also saved in txt file format.
> python nr_iqa.py

| Method  | PIQUE | BRISQUE | NIQE | PSNR | MSE |
|---------|-------|---------|------|------|-----|
|max|63.10|83.4|16.00|55.51|1003.29|
|min|35.80|48.40|10.20|30.43|0.18|
|mean|47.85|65.63|13.17|34.29|174.53| 
|median|**47.40**| **65.80**| **13.20**| **34.03**| **146.51**|

The analysed was acquired from the IIT-H Dataset, and it also can be observed that the quality of the frames achieved are fairly good but not great. The next work would be getting the optimum number of frames for analysis using the IQA.

## RESULTS & FORTHCOMING WORKS

### Full-Reference IQA

The following result is obtained using the Structural Similarity Index (SSIM) and the Mean Squared Error (MSE) and the corresponding Median is also calculated. 

<img width="297" alt="ssim_global frames" src="https://github.com/ambparth/imqua_assess/assets/45915770/26150da8-9951-4b82-998a-bfd74a400a7f">

<img width="311" alt="mse_global frames" src="https://github.com/ambparth/imqua_assess/assets/45915770/02a8623f-f521-4a8f-bfa4-b1b6ad565198">

One of the ambiguity using the FR-IQA is the reference frame (which is assumed to be the preceeding frame here in this analysis). Thus, a better way to quantize the frame is by individually scoring each and every frame. 

### No-Reference IQA

The following result is being obtained by using BRISQUE, NIQE and PIQE. Note that the data is anlaysed using the one provided by IIT-H. The video duration of the data was roughly 40 minutes, and captured at 20fps. The net frames that is achieved is approximately 35,000 in number. 

<img width="284" alt="brisque_plot" src="https://github.com/ambparth/imqua_assess/assets/45915770/7d83ca87-6ea7-4fb8-9858-af719580b396">


<img width="284" alt="niqe_plot" src="https://github.com/ambparth/imqua_assess/assets/45915770/9fb70f2d-1f46-4ae8-8cd3-7c2be7b99f84">


<img width="302" alt="PIQE_values_frames" src="https://github.com/ambparth/imqua_assess/assets/45915770/f9f7a3da-1f14-4973-8066-78b31455b6f2">

The analysis using the BRISQUE metric (left), using NIQE (middle) and PIQE (right). It can be observed that there are some subtle variable of each of the frames and the variation is almost constant in the case of NIQE and relatively present in the case of PIQE. The next step in the forthcoming work, would be take the optimum frame that gives the best information, so that the 35,000 frames can be reduced to a relatively less number,say to roughly about one-tenth of the initial count (say to about 3000 frames). 
