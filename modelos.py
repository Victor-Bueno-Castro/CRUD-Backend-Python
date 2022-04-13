#   App de clases 
class Pelicula:

    def __init__(self, nombre, duracion, genero):
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero

class Genero:

    def __init__(self, nombre):
        self.nombre = nombre

class Catalogo: #   Clase volátil

    def __init__(self, nombre):
        self.nombre = nombre
        self.peliculas = [] #   Lista vacía donde se van a almacenar las películas