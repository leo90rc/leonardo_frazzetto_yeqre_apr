import pymysql
import os, sys
import pandas as pd
from sqlalchemy import create_engine

dir = os.path.dirname
sep = os.sep
project_path = dir(dir(dir(os.path.abspath(__file__))))
sys.path.append(project_path)


from src.utils.folders_tb import read_json


def enviar_tabla_SQL(nombre_tabla, nombre_fichero):
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
        tabla_data_file_path = project_path + os.sep + 'data' + os.sep + 'tablas' + os.sep + nombre_fichero
        tabla_data_file = pd.read_csv(tabla_data_file_path)
        tabla_data_file.to_sql(name = nombre_tabla, con= db_connection, if_exists= 'replace', index=False)
        return 'La tabla ha sido insertada correctamente en la base de datos.'

class MySQL:

    def __init__(self, IP_DNS, USER, PASSWORD, BD_NAME, PORT):
        self.IP_DNS = IP_DNS
        self.USER = USER
        self.PASSWORD = PASSWORD
        self.BD_NAME = BD_NAME
        self.PORT = PORT
        self.SQL_ALCHEMY = 'mysql+pymysql://' + self.USER + ':' + self.PASSWORD + '@' + self.IP_DNS + ':' + str(self.PORT) + '/' + self.BD_NAME
    def connect(self):
        # Open database connection
        self.db = pymysql.connect(host=self.IP_DNS,
                                  user=self.USER, 
                                  password=self.PASSWORD, 
                                  database=self.BD_NAME, 
                                  port=self.PORT)
        # prepare a cursor object using cursor() method
        self.cursor = self.db.cursor()
        print("Connected to MySQL server [" + self.BD_NAME + "]")
        return self.db


 #   def close(self):
        # disconnect from server
  #      self.db.close()
   #     print("Close connection with MySQL server [" + self.BD_NAME + "]")
    

    def execute_interactive_sql(self, sql, delete=False):
        """ NO SELECT """
        result = 0
        try:
            # Execute the SQL command
            self.cursor.execute(sql)
            # Commit your changes in the database
            self.db.commit()
            print("Executed \n\n" + str(sql) + "\n\n successfully")
            result = 1
        except Exception as error:
            print(error)
            # Rollback in case there is any error
            self.db.rollback()
        return result
        '''
    def execute_get_sql(self, sql):
        """SELECT"""
        results = None
        print("Executing:\n", sql)
        try:
            # Execute the SQL command
            self.cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = self.cursor.fetchall()
        except Exception as error:
            print(error)
            print ("Error: unable to fetch data")
        
        return results

    def generate_insert_into_people_sql(self, to_insert):
        """
        This must be modified according to the table structure
        """
        nombre = to_insert[0]
        apellidos = to_insert[1]
        direccion = to_insert[2]
        edad = to_insert[3]
        nota = to_insert[4]
        
        sql = """INSERT INTO people
            (MOMENTO, NOMBRE, APELLIDOS, DIRECCION, EDAD, NOTA)
            VALUES
            (NOW(), '""" + nombre + """', '""" + apellidos + """', '""" + direccion + """', '""" + edad + """', '""" + nota + """')"""

        sql = sql.replace("\n", "").replace("            ", " ")
        return sql
        '''