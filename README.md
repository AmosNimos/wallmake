# wallmake

WallMake is a set of scripts that allow you to create a desktop wallpaper from any image, matching the size of your main monitor and with the average color of the four corners of the original image as the fill color.

## wallmake.py

wallmake.py is a Python script that uses the Pillow library to resize and center an image, and create a new image with the fill color. It requires Python 3 and the Pillow library to run.

### Usage:
~~~
python3 wallmake.py path/to/image.extension
~~~

---

## wallmake

wallmake is a Bash script that uses the ImageMagick library to accomplish the same task as wallmake.py. It requires ImageMagick to be installed on your system.

### Usage:
~~~
./wallmake path/to/image.extension
~~~

Both scripts Should create a new image file named "output.png" in the current directory.

License:

WallMake is licensed under the MIT License. Feel free to modify and distribute the scripts as you see fit, as long as you include the original license and attribution.
