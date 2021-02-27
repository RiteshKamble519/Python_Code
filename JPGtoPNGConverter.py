import sys 
import os 
from PIL import Image
#grab first and second argument from command line as current folder(JPG)name and destination folder(PNG) name 
image_folder,output_folder = sys.argv[1:]

#check if destination\(eg : 'new\') folder exist if no create a new one 
if not (os.path.exists(output_folder)):
    os.makedirs(output_folder)
    
#convert JPG to PNG
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    #if clean_name step is ignored then the file is named as pikachu.jpg.png
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png','png')
    print(filename+" converted to PNG")

# Eg command : python .\JPGtoPNGConverter.py Pokedex\ new\