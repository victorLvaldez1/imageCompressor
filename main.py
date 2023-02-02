from PIL import Image
import os

#where the images are
folder = "C:/Users/virul/Desktop/Quavanti/IMAGES_BIRLOS/Hotpot Design/CS-SICLIK-B2C/"
#Where the compressed images will be saved
folderToSave = "C:/Users/virul/Desktop/Quavanti/IMAGES_BIRLOS/Hotpot Design/compressed_images/"

if __name__ == "__main__":
    for filename in os.listdir(folder):
        name, extension = os.path.splitext(folder + filename)
        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(folder + filename)
            picture.save(folderToSave + filename, optimized=True, quality=60)
            