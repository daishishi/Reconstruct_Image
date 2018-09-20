# Reconstruct_Image

How to use:
Windows
-Open the PowerShell
-digit: cd -Path from the directory where the script is- ex: C:\Users\***\Downloads
-digit: python ImgRedo.py
-digit: the path from the directory with the images and Json files
-Wait the process finish

Dependencies:
This script runs on Python 2.7 and requires the Modules PIL and pandas
To install the modules on WINDOWS using pip:
-Open the PowerShell
-digit: python -m pip install 'module name'

Attention:

-The folder can have any other files beside the original images and json files and the script will care only with the json files and images

-Be aware that the script don't use the name of the archives to guide itself through the files into the folder, but use the total number of json files to edit a equal number of images

-As such the process is: the first json file in the folder edit the first image, the second json the second image, and so on.
-Then is wise to a folder only have the same number of json files as images, and the they share the same name.

-The images are writen in the same folder that the original images
