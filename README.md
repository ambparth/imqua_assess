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

Coming to the project here, the frames achieved are quantified with the above FR-IQA methods, with one main assumption. **The frame preceeding the other is considered or assumed as the reference.** This assumption is an arguable statement, especially in the field of autonomous vehicles as there would be multiple frames in one second that can be considered as the reference. Therefore, the idea of NR-IQA (No Reference- Image Quality Assessment) could solve this ambiguity. 

## NR-IQA (No Reference- Image Quality Assessment)
The FR-IQA gives a good estimate of the image, but the estimate is done mainly by checking the similarity of the images, which in practical case will not ply as, for istance it will be meaningless to say that blured image is somwhat similar to that of the original image. The other practical aspect to think about is the reference or Ground Truth. Like as discussed in the above paragraph, the ambiguity of ground truth presides. So therefore each and every frame has to be scored. 

### BRISQUE
This No-reference quality metric scores the image based on know distortions. Higher the score, lower the quality of image. 

### NIQE
This metric is trained purely on clean images, yet can classify the images on the quality of it. Lower the score higher the quality. 

### PIQUE
This metric on the other hand is inspired by the human perception of image assessment. Lower the score, higher is the quality. 

## CODE LAYOUT
Run this code for analysing the FR-IQA metrics on the frames. The metrics are also saved as text files for a future analysis. 
>python fr_iqa.py

Similarly for the NR-IQA methods, the functions are taken from https://github.com/guptapraful/niqe.git and https://github.com/buyizhiyou/NRVQA.git with some minor tweakings. The metrics are also saved in txt file format.
> python nr_iqa.py
