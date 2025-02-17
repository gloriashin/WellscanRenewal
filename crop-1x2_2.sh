#!/bin/bash
WIDTH=13100
HEIGHT=8730
X1=96
X2=384
Y1=768
Y2=11208

THERMO_WIDTH=500
THERMO_HEIGHT=3000
THERMO_X=0
THERMO_Y=12000

HUMID_WIDTH=3000
HUMID_HEIGHT=1500
HUMID_X=2500
HUMID_Y=0

#using -region to reduce using memory

for TIF in ./*.jpg; do
  echo "Processing file: $TIF"
  
  # Get the image dimensions (width and height)
  IMAGE_DIMENSIONS=$(identify -format "%wx%h" "$TIF")
  IMAGE_WIDTH=$(echo $IMAGE_DIMENSIONS | cut -d 'x' -f 1)
  IMAGE_HEIGHT=$(echo $IMAGE_DIMENSIONS | cut -d 'x' -f 2)
  
  echo "Image dimensions: ${IMAGE_WIDTH}x${IMAGE_HEIGHT}"

  P1="${TIF/.jpg/.P8.jpg}"
  P2="${TIF/.jpg/.P10.jpg}"
  P3="${TIF/.jpg/.P9.tif}"
  P4="${TIF/.jpg/.P11.tif}"
  THERMO="${TIF/.jpg/.thermo.jpg}"
  HUMID="${TIF/.jpg/.humid.jpg}"

  if [ ! -e "$P1" ]; then
    # Check if the crop area is within the image bounds
    if [ $IMAGE_WIDTH -ge $WIDTH ] && [ $IMAGE_HEIGHT -ge $HEIGHT ]; then
      echo "Running: convert \"$TIF\" -region ${WIDTH}x${HEIGHT}+${X1}+${Y1} -compress lzw \"$P1\""
      convert "$TIF" -region "${WIDTH}x${HEIGHT}+${X1}+${Y1}" -compress lzw "$P1"
      
      echo "Running: convert \"$TIF\" -region ${WIDTH}x${HEIGHT}+${X2}+${Y2} -compress lzw \"$P2\""
      convert "$TIF" -region "${WIDTH}x${HEIGHT}+${X2}+${Y2}" -compress lzw "$P2"
    
    else
      echo "Warning: Image $TIF is too small for cropping dimensions ${WIDTH}x${HEIGHT}. Skipping."
    fi
  else
    echo "Files already exist for $TIF, skipping cropping."
  fi
done
