import pandas as pd
import sys
import os



def columna_vs_columna(lista_dataframes, posicion_df1, posicion_df2):
    ''' Compara los nombres de las columnas de 2 dataframes que se encuentran en una lista, tomando como argumento la posición de dicho dataframe en la lista.
    
    Tener en cuenta que, para aplicarla, ambos dataframes deben tener la misma cantidad de columnas. '''
    try:
        for pos, valor in enumerate(lista_dataframes[posicion_df1].columns == lista_dataframes[posicion_df2].columns):
            if valor == False:
                print('         Posición de columna diferente: ' + str(pos))
                print('         ---------------------------------')
                print('         Columna de DF en posición ' + str(posicion_df1) + ': ' + lista_dataframes[posicion_df1].columns[pos])
                print('         Columna de DF en posición ' + str(posicion_df2) + ': ' + lista_dataframes[posicion_df2].columns[pos])
                print('         ================================================\n')
    except:
        print('Los dataframes a comparar deben tener la misma cantidad de columnas.')



def comparar_columnas(lista_dataframes): 
    ''' SE DEBE INGRESAR UNA LISTA DE DATAFRAMES A COMPARAR. '''
    for i in range(len(lista_dataframes)):
            for j in range(1, len(lista_dataframes)):    
                if i < j:
                    if len(lista_dataframes[i].columns) == len(lista_dataframes[j].columns):
                        columnas_iguales = lista_dataframes[i].columns == lista_dataframes[j].columns # TRUE si coinciden, FALSE si no
                        if all(columnas_iguales):
                            print('Las columnas de ' + str(i) + ' (' + str(len(lista_dataframes[i].columns)) +') y ' + str(j)+ ' (' + str(len(lista_dataframes[j].columns)) + ') COINCIDEN.')
                            print('======================================================')
                            break
                        else:
                            print('\nLas columnas de ' + str(i) + ' (' + str(len(lista_dataframes[i].columns)) +') y ' + str(j) + ' (' + str(len(lista_dataframes[j].columns)) + ') SON DISTINTAS.\n')
                            columna_vs_columna(lista_dataframes, i, j)
                    else:
                        print(str(i) +  ' (' + str(len(lista_dataframes[i].columns))  + ') y ' + str(j) + ' (' + str(len(lista_dataframes[j].columns)) + ') tienen distinta CANTIDAD de columnas.')
                        print('======================================================')



def nombre_cada_columna(lista_dataframes):
    tamanio_columnas = []
    for df in lista_dataframes:
        tamanio_columnas.append(len(df.columns))
        a = max(tamanio_columnas)
    for i in range(0,a):
        print('Columna en posición ' + str(i) + '\n')
        for j in range(len(lista_dataframes)):
            try:
                print('DF en posición ' + str (j) + ': ' + str(lista_dataframes[j].columns[i]))
            except:
                print('DF en posición ' + str (j) + ': No contiene columnas en la posición ' + str(i))
        print('\n-------------------------------------\n')



def crear_df_gu(lista_df_gu):
    ''' Crea un dataframe de los datos recopilados que son de interés para el estudio en cuestión. '''
    lista_numero_expediente = []
    lista_distrito = []
    lista_barrio = []
    lista_calle = []
    lista_dia_semana = []
    lista_ano = []
    lista_mes = []
    lista_dia = []
    lista_hora = []
    lista_turno = []
    lista_victimas = []
    lista_leves = []
    lista_graves = []
    lista_muertos = []
    for i in range(len(lista_df_gu)):
        for pos, value in enumerate(lista_df_gu[i].columns):
            if 'expedient' in value.lower():
                lista_numero_expediente.extend(lista_df_gu[i].iloc[:,pos])
            if ('nom' in value.lower()) and ('districte' in value.lower()):
                lista_distrito.extend(lista_df_gu[i].iloc[:,pos])
            if ('nom' in value.lower()) and ('barri' in value.lower()):
                lista_barrio.extend(lista_df_gu[i].iloc[:,pos])
            if ('nom' in value.lower()) and ('carrer' in value.lower()):
                lista_calle.extend(lista_df_gu[i].iloc[:,pos])
            if (('descripció' in value.lower()) or ('descripcio' in value.lower())) and ('setmana' in value.lower()):
                lista_dia_semana.extend(lista_df_gu[i].iloc[:,pos])
            if ('any' in value.lower()) and ('mes' not in value.lower()):
                lista_ano.extend(lista_df_gu[i].iloc[:,pos])
            if ('mes' in value.lower()) and ('nom' in value.lower()):
                lista_mes.extend(lista_df_gu[i].iloc[:,pos])
            if ('mes' in value.lower()) and ('dia' in value.lower()):
                lista_dia.extend(lista_df_gu[i].iloc[:,pos])
            if ('hora' in value.lower()) and ('dia' in value.lower()):
                lista_hora.extend(lista_df_gu[i].iloc[:,pos])
            if 'torn' in value.lower():
                lista_turno.extend(lista_df_gu[i].iloc[:,pos])
            if ('víctimes' in value.lower()) or ('victimes' in value.lower()):
                lista_victimas.extend(lista_df_gu[i].iloc[:,pos])
            if 'lleus' in value.lower():
                lista_leves.extend(lista_df_gu[i].iloc[:,pos])
            if 'greus' in value.lower():
                lista_graves.extend(lista_df_gu[i].iloc[:,pos])
            if 'morts' in value.lower():
                lista_muertos.extend(lista_df_gu[i].iloc[:,pos])
    return pd.DataFrame(list(zip(lista_numero_expediente, lista_distrito, lista_barrio, lista_calle, lista_dia_semana,
    lista_ano, lista_mes, lista_dia, lista_hora, lista_turno, lista_victimas, lista_leves, lista_graves, lista_muertos)),
    columns= ['NUMERO EXPEDIENTE', 'DISTRITO', 'BARRIO', 'CALLE', 'DIA SEMANA', 'ANO', 'MES', 'DIA', 'HORA', 'TURNO', 'NUMERO VICTIMAS',
    'VICTIMAS LEVES', 'VICTIMAS GRAVES', 'VICTIMAS FALLECIDAS'])



def quitar_espacios(df):
    '''Quita los espacios en blanco al inicio y final de los valores tipo string que contenga el dataframe que se pasa por argunto.'''
    for columna in df.columns:
        try:
            df[columna] = df[columna].str.strip()
        except:
            pass



def translate(df):
    '''Traduce del catalán al castellano los valores tipo string referidos a "día", "mes" y "turno" que contenga el dataframe que se pasa por argumento.'''
    lista_castellano = ['Mañana', 'Tarde', 'Noche', 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    lista_catalan = ['Matí', 'Tarda', 'Nit', 'Gener', 'Febrer', 'Març', 'Abril', 'Maig', 'Juny', 'Juliol', 'Agost', 'Setembre', 'Octubre', 'Novembre', 'Desembre', 'Dilluns', 'Dimarts', 'Dimecres', 'Dijous', 'Divendres', 'Dissabte', 'Diumenge']
    df.replace(lista_catalan, lista_castellano, inplace = True)