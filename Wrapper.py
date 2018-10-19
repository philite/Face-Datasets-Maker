from google_images_download import google_images_download
import os
from autocrop import autocrop

basedir = ''
space = ' '

#response = google_images_download.googleimagesdownload()
#absolute_image_paths = response.download({'keywords':'Nicolas Cage', 'limit':5, 'format':'jpg'})

#Credit to phihag for answer on how to change folder name with python 
#(https://stackoverflow.com/questions/8735312/how-to-change-folder-names-in-python)
for folder in os.listdir(basedir):
    if folder.count(space) != 0:
        print(folder)
        newName = folder.replace(space,'_')
        print(newName)
        os.rename(os.path.join(basedir, folder), os.path.join(basedir, newName))
