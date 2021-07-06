from tensorflow.keras.models import load_model
import sys
import os


dir = os.path.dirname
sep = os.sep
project_path = dir(dir(dir(os.path.abspath(__file__))))
sys.path.append(project_path)


def guardar_modelo(nombre_modelo, nombre_fichero):
    nombre_modelo.save(project_path + sep + 'models' + sep + nombre_fichero + '.h5')

def cargar_modelo(nombre_fichero):
    modelo = load_model(project_path + sep + 'models' + sep + nombre_fichero + '.h5')
    return modelo