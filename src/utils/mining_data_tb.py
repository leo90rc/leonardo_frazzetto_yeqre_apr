import sys
import os


dir = os.path.dirname
sep = os.sep
ml_project_path = dir(dir(dir(os.path.abspath(__file__))))
sys.path.append(ml_project_path)



def nombres_carpetas_ok(lista_carpetas):
    lista_carpetas_ok = []
    for i in lista_carpetas:
        i = i[10::]
        i = i.replace('-', ' ')
        i = i.replace('_', ' ')
        i = i.title()
        lista_carpetas_ok.append(i)
    return lista_carpetas_ok


def renombrar_carpetas(lista_nombres_ok):
    lista_original_carpetas = os.listdir('data/fotos_perros/train')
    for i in lista_nombres_ok:
        for j in lista_original_carpetas:
            