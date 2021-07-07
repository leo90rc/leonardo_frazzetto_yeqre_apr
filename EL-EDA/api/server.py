import argparse
from flask import Flask, request, render_template
import os
import sys
import json

dir = os.path.dirname
sep = os.sep
eda_project_path = dir(dir(dir(__file__)))
sys.path.append(eda_project_path)


from src.utils.folders_tb import read_json
from src.utils.folders_tb import csv_to_json

parser = argparse.ArgumentParser()
parser.add_argument("-x", "--x", type=int)

args = vars(parser.parse_args())

settings_file = os.path.dirname(__file__) + sep + "settings.json"
json_readed = read_json(fullpath=settings_file)

if args['x'] == json_readed["argparse"]:

    app = Flask(__name__)

    @app.route('/')
    def ingreso():
        return 'Para obtener el json del dataframe debe acceder al endpoint "/obtener_json" pasando por parámetro la contraseña correcta.\n\
            Inserte en la URL: localhost:6060/obtener_json?token_id="INSERTAR_CONTRASEÑA"'

    @app.route('/obtener_json', methods=['GET'])
    def obtener_json():
        x = request.args['token_id']
        S = json_readed["token_id"]
        if x == S:
            ubicacion_accidentes = eda_project_path + sep + 'data' + sep + 'DATA_POST_CLEANING' + sep + 'accidentes.csv'
            return csv_to_json(path_fichero = ubicacion_accidentes)
        else:
            return "La contraseña es incorrecta."


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
    print('Wrong password')