import sqlite3
from modelos import Pelicula  #   Importación de librería sqlite3

def connect_db():
    conexion = sqlite3.connect('pelis.db')    #   Generar conexión con la BD
    cursor = conexion.cursor()  #   Para ejecución de los SQL
    return conexion, cursor #   Retornar conexión y cursor

#   Funcion para agregar pelicula utilizando comando sql
def agregar_pelicula(pelicula):
    conexion, cursor = connect_db()
    pelicula = (
        pelicula.nombre,
        pelicula.duracion,
        pelicula.genero
        )
 
    sql = f'INSERT INTO pelicula(nombre, duracion, genero) VALUES{pelicula};'
    cursor.execute(sql)
    conexion.commit()
    conexion.close()

def obtener_peliculas():
    conexion, cursor = connect_db()
    sql = 'SELECT * FROM pelicula; '
    cursor.execute(sql)
    peliculas = cursor.fetchall()
    conexion.close()
    return peliculas