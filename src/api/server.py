import argparse
from flask import Flask, request, render_template
import os
import sys
import json
import pandas as pd
from sqlalchemy import create_engine


dir = os.path.dirname
sep = os.sep
project_path = dir(dir(dir(os.path.abspath(__file__))))
sys.path.append(project_path)

print('PROYECT_PATH', project_path)

from src.utils.folders_tb import read_json
from src.utils.folders_tb import csv_to_json
from src.utils.sql_tb import MySQL


parser = argparse.ArgumentParser()
parser.add_argument("-x", "--x", type=str)

args = vars(parser.parse_args())

settings_file = dir(os.path.abspath(__file__)) + sep + "settings.json"
json_readed = read_json(fullpath=settings_file)

if args['x'] == json_readed["argparse"]:

    app = Flask(__name__)

    @app.route('/')
    def ingreso():
        return 'Para obtener el json de los datos utilizados para el proyecto, debe acceder al endpoint "/data" pasando por parámetro la contraseña correcta.\n\
            Inserte en la URL: localhost:6060/data?token_id="PASSWORD".\n\nSi desea que la tabla de datos se inserte en la base de datos de MySQL, acceda al endpoint "/insert_table_sql" de la siguiente manera: "localhost:6060/insert_table_sql".\n Si desea eliminar la tabla de datos de la base de datos, acceda al endpoint "/delete_table_sql" de la siguiente manera: "localhost:6060/delete_table_sql".'

    @app.route('/data', methods=['GET'])
    def obtener_json():
        x = request.args['token_id']
        S = json_readed["token_id"]
        if x == S:
            ubicacion_data_file = project_path + sep + 'data' + sep + 'tablas' + sep + 'data_files.csv'
            return csv_to_json(path_fichero = ubicacion_data_file)
        else:
            return "La contraseña es incorrecta."

    @app.route('/insert_table_sql', methods=['GET', 'POST'])
    def table_to_MySQL():
        manage_sql_json_readed = read_json(project_path + os.sep + 'src' + os.sep + 'manage_sql.json')
        IP_DNS = manage_sql_json_readed["IP_DNS"]
        USER = manage_sql_json_readed["USER"]
        PASSWORD = manage_sql_json_readed["PASSWORD"]
        BD_NAME = manage_sql_json_readed["BD_NAME"]
        PORT = manage_sql_json_readed["PORT"]
        mysql_db = MySQL(IP_DNS=IP_DNS, USER=USER, PASSWORD=PASSWORD, BD_NAME=BD_NAME, PORT=PORT)
        mysql_db.connect()
        db_connection_str = mysql_db.SQL_ALCHEMY
        db_connection = create_engine(db_connection_str)
        tabla_data_file_path = project_path + os.sep + 'data' + os.sep + 'tablas' + os.sep + 'data_files.csv'
        tabla_data_file = pd.read_csv(tabla_data_file_path)
        tabla_data_file.to_sql(name = 'leonardo_gaston_frazzetto', con= db_connection, if_exists= 'replace', index=False)
        return 'La tabla ha sido insertada correctamente en la base de datos.'


    @app.route('/delete_table_sql', methods=['GET', 'DELETE'])
    def delete_table_sql():
        manage_sql_json_readed = read_json(project_path + os.sep + 'src' + os.sep + 'manage_sql.json')
        IP_DNS = manage_sql_json_readed["IP_DNS"]
        USER = manage_sql_json_readed["USER"]
        PASSWORD = manage_sql_json_readed["PASSWORD"]
        BD_NAME = manage_sql_json_readed["BD_NAME"]
        PORT = manage_sql_json_readed["PORT"]
        mysql_db = MySQL(IP_DNS=IP_DNS, USER=USER, PASSWORD=PASSWORD, BD_NAME=BD_NAME, PORT=PORT)
        mysql_db.connect()
        db_connection_str = mysql_db.SQL_ALCHEMY
        db_connection = create_engine(db_connection_str)
        mysql_db.execute_interactive_sql(sql="DROP TABLE IF EXISTS leonardo_gaston_frazzetto")
        return 'La tabla ha sido eliminada de la bases de datos.'


    def main():
        print("---------STARTING PROCESS---------")

        SERVER_RUNNING = json_readed["server_running"]
        print("SERVER_RUNNING", SERVER_RUNNING)
        if SERVER_RUNNING:
            DEBUG = json_readed["debug"]
            HOST = json_readed["host"]
            PORT_NUM = json_readed["port"]
            app.run(debug=DEBUG, host=HOST, port=PORT_NUM)
        else:
            print("Server settings.json doesn't allow to start server. " + 
                "Please, allow it to run it.")

    if __name__ == "__main__":
        main()

else:
    print('Contraseña incorrecta')