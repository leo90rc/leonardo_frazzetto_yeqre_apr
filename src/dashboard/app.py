import os
import sys
from PIL import Image
import streamlit as st
import pandas as pd
import numpy as np
from tensorflow import keras
import matplotlib.pyplot as plt
from tensorflow.keras import preprocessing
import time
from sqlalchemy import create_engine


dir = os.path.dirname
sep = os.sep
project_path = dir(dir(dir(os.path.abspath(__file__))))
sys.path.append(project_path)


from src.utils import models as mo_tb
from src.utils import folders_tb as f_tb
from src.utils import sql_tb





menu = st.sidebar.selectbox('Menu:', options=["Bienvenida", "Técnicas utilizadas", "Visualización", "Predicción del modelo", "Modelos de BBDD SQL"])



if menu == 'Bienvenida':
    st.title('¿Y éste qué raza es?')
    st.write('')
    st.write('Dependiendo de a quién se le pregunte, se pueden encontrar respuestas muy variadas en cuanto a la cantidad de razas de perros conocidas. Puntualmente, la respuesta que brinda la Federación Cinológica Internacional (FCI), es que existen 368 razas reconocidas a título provisional.')
    st.write('')
    st.write('Ante la gran diversidad, se presenta éste proyecto, que tiene la intención de brindar una funcionalidad que permita lograr determinar mediante la lectura de una imagen cargada por el usuario, de qué raza se trata el perro en cuestión.')
    st.write('')
    st.write('Para lograr el propósito deseado, se establecea un modelo predictivo basado en el entrenamiento de Redes Neuronales Convolucionales (CNN), que aprende de un conjunto de datos conformado por 12000 imágenes de 120 razas de perros diferentes.')
    imagen_portada = Image.open(project_path + sep + 'resources' + sep + 'fondo_perros.jpg')
    st.image(imagen_portada, use_column_width=True)

if menu == 'Técnicas utilizadas':
    st.title('Técnicas utilizadas')
    st.write('En este apartado se mostrarán algunas de las técnicas de preprocesamiento de datos utilizadas.')
    menu_prepro = st.selectbox('Técnica de preprocesamiento de datos:', options=['Reducción imágenes RGB a una dimensión de color', 'Data Augmentation'])

    if menu_prepro == 'Reducción imágenes RGB a una dimensión de color':
        st.write('Suele resultar útil en algunos casos entrenar a nuestra red neuronal con imágenes a las que se le realice previamente una transformación de RGB a una dimensión de color')
        imagenes_rgb = Image.open(project_path + sep + 'reports' + sep + 'cuadricula_rgb.png')
        st.image (imagenes_rgb,use_column_width=True)
        imagenes_gray = Image.open(project_path + sep + 'reports' + sep + 'cuadricula_gray.png')
        st.image (imagenes_gray,use_column_width=True)
    
    if menu_prepro == 'Data Augmentation':
        st.write('Data Augmentation es una técnica que suele resultar útil cuando nuestro modelo cuenta con pocos datos o bien comienza a aprender patrones irrelevantes generando *overfitting*. Consiste en realizar una serie de transformaciones a las imágenes, obteniendo nuevos datos para alimentar al modelo.')
        imagenes_dataaugmentation = Image.open(project_path + sep + 'reports' + sep + 'data_augmentation.png')
        st.image (imagenes_dataaugmentation,use_column_width=True)

if menu == "Visualización":

    st.title('Resultados logrados')
    st.write('Seleccione el modelo deseado para visualizar los resultados de *precisión* y *pérdida* obtenidos para los conjuntos de train y validación.')
    menu_modelos = st.selectbox('Modelo:', options=['Model1', 'Model2', 'Model1_aug', 'Model4'])

    if menu_modelos == 'Model1':                                         
        st.write('Model1 ha sido entrenado utilizando el conjunto de train con 3 dimensiones de color (RGB). Está basado en redes neuronales convolucionales.')
        model1_plot = Image.open(project_path + sep + 'reports' + sep + 'model1_accuracy_loss.png')
        st.image (model1_plot,use_column_width=True)
        st.write('En la gráfica de **precisión** se observa un claro *overfitting*, donde el modelo predice en un grado mucho mayor los labels del conjunto de entrenamiento, que los del conjunto de validación. Esto puede deberse a que está aprendiendo patrones no relevantes y se puede decir que el modelo no es generalizado.')
    if menu_modelos == 'Model2':
        st.write('Model2 ha sido entrenado utilizando el conjunto de train con una única dimensionalidad de color. Está basado en redes neuronales convolucionales.')
        model2_plot = Image.open(project_path + sep + 'reports' + sep + 'model2_accuracy_loss.png')
        st.image (model2_plot,use_column_width=True)
        st.write('Los resultados son muy similares caso del Model1, donde se observa un claro *overfitting*.')
    if menu_modelos == 'Model1_aug':
        st.write('Model1_aug ha sido entrenado utilizando el conjunto de train con 3 dimensiones de color (RGB). Además, con la idea de disminuir el *overfitting* observado en los modelos anteriores, se ha utilizado la técnica de Data Augmentation.')
        model1_aug_plot = Image.open(project_path + sep + 'reports' + sep + 'model1_aug_accuracy_loss.png')
        st.image (model1_aug_plot,use_column_width=True)
        st.write('Se puede visualizar la clara reducción del *overfitting*, obteniéndose así un modelo más generalizado.')
    if menu_modelos == 'Model4':
        st.write('Model4 ha sido entrennado utilizando el conjunto de train con 3 dimensiones de color (RGB). Se ha utilizado a su vez Data Augmentation para evitar el *overfitting*. Por último, se ha modificado la estructura de las capas con la idea de obtener mejores resultados.')
        model4_plot = Image.open(project_path + sep + 'reports' + sep + 'model4_accuracy_loss.png')
        st.image (model4_plot,use_column_width=True)
        st.write('El resultado final obtenido no fue el esperado, ya que el modelo arrojó los peores índices de **precisión** y **pérdida** .')

if menu == "Predicción del modelo":
    file_uploaded = st.file_uploader("Seleccione una imagen", type=['png', 'jpg', 'jpeg'])
    boton_clasificar = st.button('Clasificar')
    if file_uploaded is not None:
        image = Image.open(file_uploaded)
        st.image(image, caption='Imagen cargada', use_column_width=True)
    
    if boton_clasificar:
        if file_uploaded is None:
            st.write('Debe cargar una imagen antes de realizar la clasificación')
        else:
           

            with st.spinner('Realizando la clasificación...'):
                plt.imshow(image)
                plt.axis("off")
                file_uploaded_resized = image.resize((64, 64))
                file_uploaded_array = np.array(file_uploaded_resized)
                file_uploaded_normalized = file_uploaded_array/255
                file_uploaded_final = file_uploaded_normalized.reshape(1, 64, 64, 3)
                model = keras.models.load_model(project_path + sep + 'models' + sep + 'model1_aug.h5')
                prediccion = model.predict(file_uploaded_final)
                time.sleep(1)
                st.success('Clasificado')

                st.write(mo_tb.predecir(model,file_uploaded_final))
                

if menu == "Modelos de BBDD SQL":
    manage_sql_json_readed = f_tb.read_json(project_path + sep + 'src' + sep + 'manage_sql.json')
    IP_DNS = manage_sql_json_readed["IP_DNS"]
    USER = manage_sql_json_readed["USER"]
    PASSWORD = manage_sql_json_readed["PASSWORD"]
    BD_NAME = manage_sql_json_readed["BD_NAME"]
    PORT = manage_sql_json_readed["PORT"]
    mysql_db = sql_tb.MySQL(IP_DNS=IP_DNS, USER=USER, PASSWORD=PASSWORD, BD_NAME=BD_NAME, PORT=PORT)
    mysql_db.connect()
    db_connection_str = mysql_db.SQL_ALCHEMY
    db_connection = create_engine(db_connection_str)
    model_comparasion = pd.read_sql('SELECT * FROM model_comparasion', con=db_connection)
    st.table(model_comparasion)