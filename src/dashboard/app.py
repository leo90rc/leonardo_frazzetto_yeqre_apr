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


dir = os.path.dirname
sep = os.sep
project_path = dir(dir(dir(os.path.abspath(__file__))))
sys.path.append(project_path)


from src.utils import models as mo_tb
from src.utils import folders_tb as f_tb





menu = st.sidebar.selectbox('Menu:', options=["Bienvenida", "Visualización", "Predicción del modelo", "Modelos de BBDD SQL"])



if menu == 'Bienvenida':
    st.title('¿Y éste qué raza es?')
    st.write('')
    st.write('Dependiendo de a quién se le pregunte, podemos encontrar respuestas muy variadas en cuanto a la cantidad de razas de perros conocidas. Puntualmente, la respuesta que brinda la Federación Cinológica Internacional (FCI), es que existen 368 razas reconocidas a título provisional.')
    st.write('')
    st.write('Éste proyecto tiene la intención de establecer un modelo predictivo, el cual, basándose en el entrenamiento de Redes Neuronales Convolucionales, lograr determinar mediante la lectura de una imagen cargada por el usuario, de qué raza se trata el perro en cuestión. La red neuronal ha sido entrenada con 120 razas diferentes.')
    st.write('')



if menu == "Visualización":

    st.title('Accidentes de tráfico registrados por la Guardia Urbana de la ciudad de Barcelona en sus barrios más turísticos')
    st.write('En la siguiente sección se presentan, evaluados por cada mes, los accidentes de tráfico registados por la Guardia Urbana de la ciudad de Barcelona, para los barrios de mayor concurrencia de turistas en los meses de temporada alta.')
    menu_barrios = st.selectbox('Barrios:', options=['Seleccione un barrio', 'El Barri Gòtic', 'La Barceloneta', 'El Poble Sec', 'El Poblenou',
'Sant Pere, Santa Caterina i la Ribera', 'La Sagrada Família',
'La Nova Esquerra de l\'Eixample', 'El Fort Pienc', "L'Antiga Esquerra de l'Eixample",
'La Dreta de l\'Eixample', 'Sant Antoni', 'la Vila de Gràcia'])

    if menu_barrios == 'El Barri Gòtic':                                         
        st.write('BARRIO GÓTIC')
        gotic = Image.open(project_path + sep + 'reports' + sep + 'plots' + sep + 'gotic_x_mes.png')
        st.image (gotic,use_column_width=True)
    if menu_barrios == 'La Barceloneta':
        st.write('BARRIO DE LA BARCELONETA')
        barceloneta = Image.open(project_path + sep + 'reports' + sep + 'plots' + sep + 'barceloneta_x_mes.png')
        st.image (barceloneta,use_column_width=True)
    if menu_barrios == 'El Poble Sec':
        st.write('BARRIO DE EL POBLE SEC')
        poble_sec = Image.open(project_path + sep + 'reports' + sep + 'plots' + sep + 'poble_sec_x_mes.png')
        st.image (poble_sec,use_column_width=True)

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
                #file_uploaded_array = preprocessing.image.img_to_array(file_uploaded)
                file_uploaded_array = np.array(file_uploaded_resized)
                file_uploaded_normalized = file_uploaded_array/255
                file_uploaded_final = file_uploaded_normalized.reshape(1, 64, 64, 3)
                model = keras.models.load_model(project_path + sep + 'models' + sep + 'model1_aug.h5')
                prediccion = model.predict(file_uploaded_final)
                time.sleep(1)
                st.success('Clasificado')

                st.write(mo_tb.predecir(model,file_uploaded_final))
                


#    st.write('Directorio de destino: EDA_Project_Accidents/data/API_Download')
#    st.write('Nombre fichero: accidentes_barcelona_2010-2020.csv')
#    dataframe_accidentes = pd.read_json('http://localhost:6060/obtener_json?token_id=Y6571256D')
#    st.table(dataframe_accidentes)
#    dataframe_accidentes.to_csv(project_path + '/data/API_Download/accidentes_barcelona_2010-2020.csv', index = False, encoding = 'utf-8')

if menu == "Modelos de BBDD SQL":
    pass