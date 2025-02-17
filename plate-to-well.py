#!/usr/bin/env python
import os
import sys
import json
from PIL import Image, ImageDraw
import numpy as np

# Disable DecompressionBombWarning
Image.MAX_IMAGE_PIXELS = None

def main():
    if len(sys.argv) < 2:
        sys.stderr.write("Usage: python script.py <tiff_filename> [96]\n")
        sys.exit(1)

    filename_tif = sys.argv[1]
    filename_base = os.path.splitext(filename_tif)[0]
    filename_conf = '/home/seungyun/git/wellscan/plate-to-well.json.2400dpi96well'

    # Check if configuration file exists
    if not os.path.isfile(filename_conf):
        sys.stderr.write(f'{filename_conf} does not exist.\n')
        sys.exit(1)

    # Read configuration
    with open(filename_conf, 'r') as f_conf:
        conf = json.load(f_conf)

    # Validate configuration
    conf_param = ['rotate_angle', 'x0', 'y0', 'width', 'height', 'flip_vertical', 'flip_horizontal', 'columns', 'rows']
    for param in conf_param:
        if param not in conf:
            sys.stderr.write(f'{param} parameter does not exist. Please check the format.\n')
            sys.exit(1)

    # Open and process image
    with Image.open(filename_tif) as im:
        # Apply flips if needed
        if int(conf['flip_horizontal']) > 0:
            im = im.transpose(Image.FLIP_LEFT_RIGHT)
        if int(conf['flip_vertical']) > 0:
            im = im.transpose(Image.FLIP_TOP_BOTTOM)
        im.save(f'{filename_base}.flip.jpg', 'jpeg', quality=50)

        # Rotate and crop
        rotate_angle = float(conf['rotate_angle'])
        if rotate_angle != 0:
            # GIMP rotate and PIL rotate are opposite for the sign of angle
            im = im.rotate(rotate_angle * -1.0, expand=1)
        
        

        # Draw grid
        x_max, y_max = im.size
        cols, rows = int(conf['columns']), int(conf['rows'])
        x_well_size, y_well_size = int(conf['width']), int(conf['height'])

        im_draw = im.copy()
        draw = ImageDraw.Draw(im_draw)
        for col in range(cols + 1):
            x = int(x_well_size * col)
            draw.line((x, 0, x, y_max), fill=200, width=5)
        for row in range(rows + 1):
            y = int(y_well_size * row)
            draw.line((0, y, x_max, y), fill=200, width=5)

        im_draw = im_draw.resize((int(x_max * 0.10), int(y_max * 0.10)), Image.LANCZOS)
        im_draw.save(f'{filename_base}.grid.jpg', 'jpeg', quality=50)

        # Process individual wells if '96' argument is provided
        if len(sys.argv) > 2 and sys.argv[2] == '96':
            process_wells(im, filename_base, cols, rows, x_well_size, y_well_size)

def process_wells(im, filename_base, cols, rows, x_well_size, y_well_size):
    row_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    for col in range(cols):
        for row in range(rows):
            x1 = int(x_well_size * col)
            y1 = int(y_well_size * row)
            x2 = int(x_well_size * (col + 1))
            y2 = int(y_well_size * (row + 1))
            dir_name = f'{row_list[row]}{col+1:02d}'
            
            os.makedirs(dir_name, mode=0o755, exist_ok=True) 
            #creates a directory with specific permissions, doesn't raise an error if the directory already exists
            
            im_well = im.crop((x1, y1, x2, y2))
            im_well.save(os.path.join(dir_name, f'{filename_base}_{row_list[row]}{col+1:02d}.jpg'), 'jpeg')

if __name__ == "__main__":
    main()