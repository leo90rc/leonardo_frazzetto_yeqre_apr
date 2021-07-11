import sys
import os
import cv2
import numpy as np
import tensorflow as tf
import json
import pandas as pd
from PIL import Image

dir = os.path.dirname
sep = os.sep
project_path = dir(dir(dir(os.path.abspath(__file__))))
sys.path.append(project_path)


def cargar_imagenes_diccionario(path):
    '''Carga las imágenes que se encuentran dentro de un directorio específico recorriendo todas las carpetas que contenga.
    Parámetro: path: el path de la carpeta raiz de la cual se quieren cargar las imágenes.
    Retorna un diccionario con el label como key y la un array de la imagen como value'''
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


def cargar_imagenes_and_labels(razas, path_set):
    '''Carga imágenes recorriendo las carpetas de un determinado directorio.
    Parámetros: - razas: lista con los nombres (string) de las carpetas que contienen las imágenes a cargar.
                - path_set: path de la carpeta raiz que contiene las carpetas donde se encuentran las imágenes a cargar.
    Retorna:- Una lista con las imágenes cargadas como arrays.
            - Una lista con los labels de cada una de las imágenes'''
    lista_imagenes = []
    lista_labels = []
    for i, raza in enumerate(razas):
        for image_name in os.listdir(path_set + sep + raza):
            imagen = cv2.imread(path_set + sep + raza + sep + image_name)
            imagen_foto = Image.fromarray(imagen)
            resized_imagen_foto = imagen_foto.resize((64, 64))
            lista_imagenes.append(np.array(resized_imagen_foto))
            lista_labels.append(i)

    return lista_imagenes, lista_labels


def df_metadata(razas, path_set):
    lista_filenames = []
    lista_labels = []
    lista_resolucion = []
    for i, raza in enumerate(razas):
        for image_name in os.listdir(path_set + sep + raza):
            imagen = cv2.imread(path_set + sep + raza + sep + image_name)
            lista_labels.append(raza)
            lista_filenames.append(image_name)
            lista_resolucion.append((imagen.shape[0], imagen.shape[1]))

    df_data = pd.DataFrame(data= {'Filename': lista_filenames, 'Resolución': lista_resolucion, 'Etiqueta': lista_labels})
    return df_data


def preparar_imagen_predecir(nombre_foto, path_foto = ('..' + os.sep + 'data' + os.sep + 'fotos_perros' + os.sep + 'to_predict' + os.sep)):
    foto_predecir = cv2.imread(path_foto + nombre_foto)
    foto_predecir = Image.fromarray(foto_predecir)
    foto_predecir_resized = np.array(foto_predecir.resize((64, 64)))
    foto_predecir_normalized = foto_predecir_resized/255
    foto_predecir_final = foto_predecir_normalized.reshape(1, 64, 64, 3)
    return foto_predecir_final


def excel_resources_df(nombre_archivo):
    ''' Lee un archivo .xlsx ubicado en la dirección /resources y lo carga como un dataframe.
        Arg: nombre_archivo: Nombre del archivo que se desea abrir en string (se debe agregar ".xlsx"). '''
    global df
    df = pd.read_excel(project_path + sep + 'resources' + sep + nombre_archivo)
    return df