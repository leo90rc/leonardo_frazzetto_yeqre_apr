import sys
import os
import cv2
import numpy as np
import tensorflow as tf

dir = os.path.dirname
sep = os.sep
project_path = dir(dir(dir(os.path.abspath(__file__))))
sys.path.append(project_path)


def cargar_imagenes_diccionario(path):      # NO UTILIZADAAAAAAAAAAAAAAAA
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
            #dir_images = np.array(dir_images)
        dir_images = np.array(dir_images)
        dict_imagenes[my_key] = dir_images
    return dict_imagenes


def cargar_imagenes_tf(batch_size, img_height, img_width, data_dir, val_split, seed):
    
    batch_size = batch_size
    img_height = img_height
    img_width = img_width
    data_dir = data_dir
    
    if val_split == 0:

        train_ds = tf.keras.preprocessing.image_dataset_from_directory(data_dir,                                                                                                                                  
                                                                       seed=seed,
                                                                       image_size=(img_height, img_width),
                                                                       batch_size=batch_size)
        return train_ds

    train_ds = tf.keras.preprocessing.image_dataset_from_directory(data_dir,
                                                                   validation_split=val_split,
                                                                   subset="training",
                                                                   seed=seed,
                                                                   image_size=(img_height, img_width),
                                                                   batch_size=batch_size)

    val_ds = tf.keras.preprocessing.image_dataset_from_directory(data_dir,
                                                                 validation_split=val_split,
                                                                 subset="validation",
                                                                 seed=seed,
                                                                 image_size=(img_height, img_width),
                                                                 batch_size=batch_size)

    return train_ds, val_ds