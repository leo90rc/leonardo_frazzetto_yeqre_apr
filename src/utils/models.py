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

def enlistar_predicciones(prediccion_modelo):
    lista_predicciones = []
    for numero_prediccion in range(0, prediccion_modelo.shape[0]):
        prediccion_raza = prediccion_modelo[numero_prediccion].argmax()
        lista_predicciones.append(prediccion_raza)
    return lista_predicciones


def predecir(modelo, foto_predecir):
    raza_list = os.listdir(project_path + sep + 'data' + sep + 'fotos_perros' + sep + 'train')
    prediccion = modelo.predict(foto_predecir)
    prediccion = raza_list[prediccion.argmax()]
    return prediccion
    

