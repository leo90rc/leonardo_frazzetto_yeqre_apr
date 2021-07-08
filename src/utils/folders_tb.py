import sys
import os
import cv2
import numpy as np
import tensorflow as tf
import json
import pandas as pd

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


def read_json(fullpath):
    '''Lee y retorna un fichero ".json". Se debe pasar como argumento la dirección del fichero.'''
    with open(fullpath, "r") as json_file_readed:
        json_readed = json.load(json_file_readed)
    return json_readed



def df_to_csv(df, nombre_archivo):
    ''' Guarda dataframes como CSV en la carpeta "data_generated". 
        Args:
            - df: El dataframe que se desea guardar.
            - nombre_archivo: Nombre que recibirá el archivo guardado. Debe ser un string finalizado en ".csv".'''
    df.to_csv('../data/tablas/' + nombre_archivo, index = False, encoding = 'utf-8')



def csv_to_json(path_fichero):
    '''Retorna archivo ".json" partiendo de un ".csv". Por parámetro debe ingresarse la dirección del fichero CSV.'''
    dataframe_ml = pd.read_csv(path_fichero)
    json_ml = dataframe_ml.to_json(indent = 4)
    return json_ml