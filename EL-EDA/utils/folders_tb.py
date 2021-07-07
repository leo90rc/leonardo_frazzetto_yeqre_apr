import pandas as pd
import sys
import os
import json


dir = os.path.dirname
sep = os.sep
eda_project_path = dir(dir(dir(__file__)))
sys.path.append(eda_project_path)



def enlistar_dataframes(porcion_fichero):
    ''' El argumento debe ser la porción del fichero correspondiente (str). La misma es todo el fragmento del fichero que se encuentra entre los años.
    Ejemplo: Para el fichero "2016_ACCIDENTS_GU_BCN_2016.csv", se debe ingresar "_ACCIDENTS_GU_BCN_"'''
    lista_df = []
    if porcion_fichero == '_ACCIDENTS_GU_BCN_':
        folder = 'ACCIDENTES_GU'
    for i in range(2010,2021):
        try:
            i = pd.read_csv(eda_project_path + sep + 'data' + sep + 'TO_WRANGLING' + sep + folder + sep + str(i) + sep + str(i) + porcion_fichero + str(i) + '-utf8.csv')
        except:
            try:
                i = pd.read_csv(eda_project_path + sep + 'data' + sep + 'TO_WRANGLING' + sep + folder + sep + str(i) + sep + str(i) + porcion_fichero + str(i) +'-utf8.csv', sep=';')
            except:
                i = pd.read_excel(eda_project_path + sep + 'data' + sep + 'TO_WRANGLING' + sep + folder + sep + str(i) + sep + str(i) + porcion_fichero + str(i) +'.xlsx')
        lista_df.append(i)
    return lista_df



def df_to_csv_post_cleaning(df, nombre_archivo):
    ''' Guarda dataframes como CSV en la carpeta DATA_POST_CLEANING. 
        Args:
            - df: El dataframe que se desea guardar.
            - nombre_archivo: Nombre que recibirá el archivo guardado. Debe ser un string finalizado en ".csv".'''
    df.to_csv('../data/DATA_POST_CLEANING/' + nombre_archivo, index = False, encoding = 'utf-8')



dir = os.path.dirname
sep = os.sep
eda_project_path = dir(dir(dir(__file__)))
sys.path.append(eda_project_path)

def leer_csv_post_cleaning(nombre_archivo):
    ''' Lee un archivo .csv ubicado en la dirección /data/DATA_POST_CLEANING y lo carga como un dataframe.
        Arg: nombre_archivo: Nombre del archivo que se desea abrir en string (se debe agregar ".csv"). '''
    global df
    df = pd.read_csv(eda_project_path + sep + 'data' + sep + 'DATA_POST_CLEANING' + sep + nombre_archivo)
    return df



def read_json(fullpath):
    '''Lee y retorna un fichero ".json". Se debe pasar como argumento la dirección del fichero.'''
    with open(fullpath, "r") as json_file_readed:
        json_readed = json.load(json_file_readed)
    return json_readed



def csv_to_json(path_fichero):
    '''Retorna archivo ".json" partiendo de un ".csv". Por parámetro debe ingresarse la dirección del fichero CSV.'''
    dataframe_accidentes = pd.read_csv(path_fichero)
    dataframe_accidentes = dataframe_accidentes.head(5000)
    json_accidentes = dataframe_accidentes.to_json(indent = 4)
    return json_accidentes


def excel_resources_df(nombre_archivo):
    ''' Lee un archivo .xlsx ubicado en la dirección /resources y lo carga como un dataframe.
        Arg: nombre_archivo: Nombre del archivo que se desea abrir en string (se debe agregar ".xlsx"). '''
    global df
    df = pd.read_excel(eda_project_path + sep + 'resources' + sep + nombre_archivo)
    return df
