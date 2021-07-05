import sys
import os


dir = os.path.dirname
sep = os.sep
project_path = dir(dir(dir(os.path.abspath(__file__))))
sys.path.append(project_path)

def nombres_carpetas_ok(lista_carpetas):
    lista_carpetas_ok = []
    for i in lista_carpetas:
        i = i[10::]
        i = i.replace('-', ' ')
        i = i.replace('_', ' ')
        i = i.title()
        lista_carpetas_ok.append(i)
    return lista_carpetas_ok


def renombrar_carpetas(set_to_rename):
    for carpeta in os.listdir(project_path + sep + 'data' + sep + 'fotos_perros' + sep + set_to_rename):
        nueva_carpeta = carpeta[10::]
        nueva_carpeta = nueva_carpeta.replace('-', ' ')
        nueva_carpeta = nueva_carpeta.replace('_', ' ')
        nueva_carpeta = nueva_carpeta.title()
        os.rename(project_path + sep + 'data' + sep + 'fotos_perros' + sep + set_to_rename + sep + carpeta, project_path + sep + 'data' + sep + 'fotos_perros' + sep + set_to_rename + sep + nueva_carpeta)
            