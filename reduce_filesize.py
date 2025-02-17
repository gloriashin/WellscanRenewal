import os
import cv2
import numpy as np
path = '/media/seungyun/8TBHardDisk/scanner/250129_XT/'
#filename_tif = '/work/taejoon/Dropbox/Public/pub/XenopusIn96_2014feb04_day3.tif'
filenames = os.listdir('/media/seungyun/8TBHardDisk/scanner/250129_XT/')
filenames_tif = [x for x in filenames if '.jpg' in x]
max_pixels = 89478485 

def resize_image(input_path, output_path, max_pixels):
    # Read the image
    img = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)
    
    if img is None:
        print(f"Error: Unable to read the image at {input_path}")
        return 89478485
    
    # Get original dimensions
    height, width = img.shape[:2]
    
    # Calculate current number of pixels
    current_pixels = width * height
    
    # Calculate the scaling factor
    scale_factor = (max_pixels / current_pixels) ** 0.5
    
    # Calculate new dimensions
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)
    
    # Resize the image using INTER_AREA interpolation
    resized_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)
    
    # Save the resized image
    cv2.imwrite(output_path, resized_img, [cv2.IMWRITE_TIFF_COMPRESSION, 5])
    
    print(f"Resized image saved to {output_path}")
    print(f"New image size: {new_width}x{new_height}")

for x in filenames_tif:
    input_file = "/media/seungyun/8TBHardDisk/scanner/250129_XT/%s" %(x)
    output_file = "/media/seungyun/8TBHardDisk/scanner/250129_XT_reduced/reduced_%s" %(x)
 

    # Resize the image
    resize_image(input_file, output_file, max_pixels)
