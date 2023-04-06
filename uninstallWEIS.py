
# This script is used to remove all build and cache related files in the WEIS directory.
# This sometimes helps with odd install or runtime errors, but should not be run each 
#   time you re-compile, as it will affect the compile time significantly. 

# Author: Gerrit Motes, Sandia National Labs, April 6th 2023

import os

os.system("rm -rf build")
os.system("rm -rf */build")
os.system("rm -rf *.egg-info")
os.system("rm -rf */*.egg-info")
os.system("rm -rf */meson_build")
os.system("rm -rf local")
os.system("rm -rf */*__pycache__*")
os.system("rm -rf *.DS_Store")
os.system("rm -rf */*.DS_Store")

os.system("echo WEIS build files successfully uninstalled!")