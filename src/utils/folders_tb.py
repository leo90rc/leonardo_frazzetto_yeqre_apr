import sys
import os
import cv2

dir = os.path.dirname
sep = os.sep
project_path = dir(dir(dir(os.path.abspath(__file__))))
sys.path.append(project_path)


def cargar_imagenes_diccionario(path):
    dict_imagenes = {}
    for root, dirs, files in os.walk(path):
        #print(os.path.basename(root))
        my_key = os.path.basename(root)
        if my_key == '':
            continue
        dir_images = []
        for file_ in files:
            full_file_path = os.path.join(root, file_)
            img = cv2.imread(full_file_path)
            # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            dir_images.append(img)

        dict_imagenes[my_key] = dir_images
    return dict_imagenes