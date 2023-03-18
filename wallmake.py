#!/usr/bin/env python3

from PIL import Image
import subprocess

# Get the main monitor size
xrandr_output = subprocess.check_output(['xrandr', '--query']).decode()
primary_monitor_line = [line for line in xrandr_output.split('\n') if 'primary' in line][0]
screen_width, screen_height = [int(val) for val in primary_monitor_line.split()[2].split('+')[0].split('x')]

# Get the image size and color
image = Image.open(sys.argv[1])
image_width, image_height = image.size
image_color = image.getpixel((0, 0))

# Calculate the center coordinates
center_x = (screen_width - image_width) // 2
center_y = (screen_height - image_height) // 2

# Create the background image
background = Image.new('RGB', (screen_width, screen_height), image_color)
background.save('background.png')

# Compose the images
composite_command = ['composite', '-geometry', f'+{center_x}+{center_y}', sys.argv[1], 'background.png', 'output.png']
subprocess.run(composite_command)

# Remove the background image
subprocess.run(['rm', 'background.png'])
