import os
import sys
dir = os.path.dirname
sep = os.sep
eda_project_path = dir(dir(dir(__file__)))
sys.path.append(eda_project_path)
from PIL import Image
import streamlit as st
import pandas as pd
import numpy as np




menu = st.sidebar.selectbox('Menu:', options=["Bienvenida", "Accidentes en cada barrio", "API"])



if menu == 'Bienvenida':
    st.title('Tráfico y turistas: ¿Un cóctel explosivo?')
    st.write('')
    st.write('La ciudad de Barcelona se ubica entre uno de los destinos predilectos a la hora de hacer turismo en España. Sumado a esto, suele tratarse además de uno de los sitios preferidos a la hora de emigrar, influyendo en esta decisión factores como ser el idioma, la ubicación geográfica, la cultura y la facilidad a la hora de insertarse en la sociedad, entre otros.')
    st.write('')
    st.write('A pesar de contar con medios de transporte públicos muy efectivos (metros, ferrocarriles, teleféricos, entre otros) que luchan por apaciguar el gran caudal de personas que se desplazan de un lado a otro, es cierto que muchos continúan eligiendo su transporte personal para transitar por la ciudad.')
    st.write('')
    st.write('A lo largo del año, pero principalmente en los meses en los que el clima más acompaña, Barcelona recibe un abultado número de turistas que se aprovechan de su geografía para disfrutar de unas vacaciones inolvidables. De esta manera, al llegar los meses de temporada alta, se puede notar que el volumen de personas aumenta por encima de lo habitual en las zonas mayor atractivo turístico.')
    st.write('')
    st.write('Se intenta evaluar qué influencia tiene esta muchedumbre en la cantidad de accidentes de tráfico que se registran en la ciudad, teniendo en cuenta que, al momento de trasladarse, los turistas tienen, entre las tantas opciones, la posibilidad de elegir transportes particulares para movilizarse, como ser vehículos, ciclomotores o bicicletas de alquiler, sin descartar que los peatones también son una fuente generadora de siniestros, más aun si desconocen la ciudad.')
    st.write('')
    st.write('Para realizar foco sobre un objeto de estudio, se plantea la siguiente hipótesis:')
    st.write('')
    st.markdown('**Durante los meses de temporada alta (Julio, Agosto y Septiembre), se registran mayor cantidad de accidentes de tráfico en las zonas más turísticas de la ciudad de Barcelona.**')




if menu == "Accidentes en cada barrio":

    st.title('Accidentes de tráfico registrados por la Guardia Urbana de la ciudad de Barcelona en sus barrios más turísticos')
    st.write('En la siguiente sección se presentan, evaluados por cada mes, los accidentes de tráfico registados por la Guardia Urbana de la ciudad de Barcelona, para los barrios de mayor concurrencia de turistas en los meses de temporada alta.')
    menu_barrios = st.selectbox('Barrios:', options=['Seleccione un barrio', 'El Barri Gòtic', 'La Barceloneta', 'El Poble Sec', 'El Poblenou',
'Sant Pere, Santa Caterina i la Ribera', 'La Sagrada Família',
'La Nova Esquerra de l\'Eixample', 'El Fort Pienc', "L'Antiga Esquerra de l'Eixample",
'La Dreta de l\'Eixample', 'Sant Antoni', 'la Vila de Gràcia'])

    if menu_barrios == 'El Barri Gòtic':                                         
        st.write('BARRIO GÓTIC')
        gotic = Image.open(eda_project_path + sep + 'reports' + sep + 'plots' + sep + 'gotic_x_mes.png')
        st.image (gotic,use_column_width=True)
    if menu_barrios == 'La Barceloneta':
        st.write('BARRIO DE LA BARCELONETA')
        barceloneta = Image.open(eda_project_path + sep + 'reports' + sep + 'plots' + sep + 'barceloneta_x_mes.png')
        st.image (barceloneta,use_column_width=True)
    if menu_barrios == 'El Poble Sec':
        st.write('BARRIO DE EL POBLE SEC')
        poble_sec = Image.open(eda_project_path + sep + 'reports' + sep + 'plots' + sep + 'poble_sec_x_mes.png')
        st.image (poble_sec,use_column_width=True)
    if menu_barrios == 'El Poblenou':
        st.write('BARRIO DE EL POBLENOU')
        poblenou = Image.open(eda_project_path + sep + 'reports' + sep + 'plots' + sep + 'poblenou_x_mes.png')
        st.image (poblenou,use_column_width=True)
    if menu_barrios == 'Sant Pere, Santa Caterina i la Ribera':
        st.write('BARRIO SANT PERE, SANTA CATERINA I LA RIBERA')
        ribera = Image.open(eda_project_path + sep + 'reports' + sep + 'plots' + sep + 'ribera_x_mes.png')
        st.image (ribera,use_column_width=True)
    if menu_barrios == 'La Sagrada Família':
        st.write('BARRIO DE LA SAGRADA FAMÍLIA')
        sagrada = Image.open(eda_project_path + sep + 'reports' + sep + 'plots' + sep + 'sagrada_x_mes.png')
        st.image (sagrada,use_column_width=True)
    if menu_barrios == 'La Nova Esquerra de l\'Eixample':
        st.write('BARRIO DE LA NOVA ESQUERRA DE L\'EIXAMPLE')
        nova_esquerra = Image.open(eda_project_path + sep + 'reports' + sep + 'plots' + sep + 'nova_esquerra_x_mes.png')
        st.image (nova_esquerra,use_column_width=True)
    if menu_barrios == 'El Fort Pienc':
        st.write('BARRIO DE EL FORT PIENC')
        fort_pienc = Image.open(eda_project_path + sep + 'reports' + sep + 'plots' + sep + 'fort_pienc_x_mes.png')
        st.image (fort_pienc,use_column_width=True)
    if menu_barrios == "L'Antiga Esquerra de l'Eixample":
        st.write('BARRIO DE L\'ANTIGA ESQUERRA DE L\'ANTIGA ESQUERRA DE L\'EIXAMPLE')
        antigua_esquerra = Image.open(eda_project_path + sep + 'reports' + sep + 'plots' + sep + 'antigua_esquerra_x_mes.png')
        st.image (antigua_esquerra,use_column_width=True)
    if menu_barrios == 'La Dreta de l\'Eixample':
        st.write('BARRIO DE LA DRETA DE L\'EIXAMPLE')
        dreta = Image.open(eda_project_path + sep + 'reports' + sep + 'plots' + sep + 'dreta_x_mes.png')
        st.image (dreta,use_column_width=True)
    if menu_barrios == 'Sant Antoni':
        st.write('BARRIO SANT ANTONI')
        sant_antoni = Image.open(eda_project_path + sep + 'reports' + sep + 'plots' + sep + 'sant_antoni_x_mes.png')
        st.image (sant_antoni,use_column_width=True)
    if menu_barrios == 'la Vila de Gràcia':
            st.write('BARRIO DE LA VILA DE GRACIA')
            vila_gracia = Image.open(eda_project_path + sep + 'reports' + sep + 'plots' + sep + 'vila_gracia_x_mes.png')
            st.image (vila_gracia,use_column_width=True)

if menu == "API":
    st.title('WEB APP')
    st.write('La descarga del CSV comenzará automáticamente.')
    for i in range(2): st.write("")
    st.write('Directorio de destino: EDA_Project_Accidents/data/API_Download')
    st.write('Nombre fichero: accidentes_barcelona_2010-2020.csv')
    dataframe_accidentes = pd.read_json('http://localhost:6060/obtener_json?token_id=Y6571256D')
    st.table(dataframe_accidentes)
    dataframe_accidentes.to_csv(eda_project_path + '/data/API_Download/accidentes_barcelona_2010-2020.csv', index = False, encoding = 'utf-8')