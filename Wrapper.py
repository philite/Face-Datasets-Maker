from google_images_download import google_images_download
import os
from autocrop import autocrop

basedir = '/Users/philp/Desktop/ImageDownload_Autocrop/downloads'
space = ' '

#response = google_images_download.googleimagesdownload()
#absolute_image_paths = response.download({'keywords':'Nicolas Cage', 'limit':5, 'format':'jpg'})

for folder in os.listdir(basedir):
    if folder.count(space) != 0:
        print(folder)
        newName = folder.replace(space,'_')
        print(newName)
        os.rename(os.path.join(basedir, folder), os.path.join(basedir, newName))