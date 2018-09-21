#Write a program to rename all the files in a directory and convert them
#into .jpg file format.

import os
files = os.listdir('path or os.curdir if u want current directory')
for file in files:

    newfile = file.replace(file.split('.')[1], 'jpg')
    os.rename(file, newfile)
print(os.listdir(os.curdir))

# at path the path of the folder should be given
