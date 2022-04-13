import funciones
while True:
    try:
        menu = int(input('''
            [1] Agregar nueva película
            [2] Obtener película
            [0] Salir del sistema
        '''))

        if menu == 1:
            funciones.agregar_pelicula()    #   ignora la condicion y continua con el programa
            print('Se ha agregado la película de forma existosa')
        elif menu == 2:
            funciones.obtener_peliculas()
        elif menu > 2:
            print('Opción fuera del sistema\nIntentalo de nuevo.')
        elif menu == 0:
            print('Has salido del sistema...')
            exit()  #   Fin del ciclo while
    except ValueError as err:
        print('Ingrese una opcion válida')