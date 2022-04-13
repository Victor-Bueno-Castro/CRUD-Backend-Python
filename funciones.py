#   Funcion para agregar película
from modelos import Pelicula, Genero, Catalogo  #   Importación de las clases
import sql

def agregar_pelicula(): #   Función que agrega películas

    nombre = str(input('Ingresa el nombre de la pelicula: '))
    duracion = int(input('Ingresa la duración de la película: '))
    genero = int(input('Ingresa el genero de la pelicula: '))

    #   Instancia de los objetos
    pelicula = Pelicula(nombre, duracion, genero)
    sql.agregar_pelicula(pelicula)

catalogo = Catalogo('Peliculas de Mafia')
def obtener_peliculas():
    peliculas = sql.obtener_peliculas()
    for pelicula in peliculas:
        guardar_pelicula = Pelicula(pelicula[1], pelicula[2], pelicula[3])
        catalogo.peliculas.append(guardar_pelicula)

    for pelicula in catalogo.peliculas:
        print(f'''\n
            Nombre de la pelicula: {pelicula.nombre}
            Duracion de la pelicula: {pelicula.duracion}  minutos
            Genero de la pelicula: {pelicula.genero}
        ''')