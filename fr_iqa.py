#%% Import the library here.
import os 
from math import log10, sqrt
import numpy as np
import natsort
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import mean_squared_error
from brisque import BRISQUE

#%% The directory of the data that is the frames. 
frame_path = 'PATH/OF/FRAMES/'
a1 = os.listdir(frame_path)
a1 = natsort.natsorted(a1) # proper number wise sorting. 


#%% Using FR-IQA (Full Reference- Image Quality Assessment); 
# Structural Similarity Index (SSIM), Mean Squared Error (MSE) & Peak Signal-to-Noise Ration (PSNR)
def PSNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if(mse == 0):
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr

ssim_vals = []
mse_vals = []
for i in np.arange(len(a1)-1):
  img1 = plt.imread(frame_path+a1[i]); 
  img2 = plt.imread(frame_path+a1[i+1]);
  ssim_img = ssim(img1,img2,data_range = img1.max()-img1.min()) #ssim
  mse_img = mean_squared_error(img1,img2) #mse
  psnr_img = PSNR(img1,img2) # psnr
  ssim_vals.append(ssim_img)
  mse_vals.append(mse_img)
  psnr_vals.append(psnr_img)
np.savetxt('ssim_vals.txt',ssim_vals)
np.savetxt('mse_vals.txt',mse_vals)
np.savetxt('psnr_vals.txt',psnr_vals)
print('Done with the FR-IQA analysis of the frames');

  

  
