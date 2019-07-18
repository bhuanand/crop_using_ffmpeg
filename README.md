# Crop part of a mp4 file using ffmpeg
This file can be used to crop an interval from an input file using ffmpeg

you can import the file or call the function by loading it in interpreter.

```
~ python
Python 2.7.12 (default, Nov 12 2018, 14:36:49) 
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import crop
>>> crop.crop_and_save("00:00:04","01:04:08", "sample.mp4")
```
