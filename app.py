
import conexion
import querys as q

exec(open("conexion.py").read())#auto-ejecuta el fichero conexion.py

#conexion=sqlite3.connect("bd1.db")

#---- Zona de funciones ----

def insertar_peli():

    print("insertar pelicula")

    titulo = input("Ingresar titulo: ")
    direccion = input("Ingresar Direccion: ")
    produccion = input("Ingresar Produccion: ")
    musica = input("Ingresar Musica: ")
    pais = input("Ingresar Pais de origen: ")
    anio = int(input("Ingresar año de estreno: "))
    genero = input("Ingresar Género: ")
    sinopsis = input("Ingresar Sinopsis: ")

    q.insert(titulo, direccion, produccion, musica, pais, anio, genero, sinopsis)


def listar_peli():

    print("Listar peliculas")

    q.select_all()



def print_menu():

    print("====================")
    print(" CRUD DE PELÍCULAS ")
    print("====================")
    print(" Elegir una opción")
    print("")
    print("[1] listar peliculas")
    print("[2] add new pelicula")
    print("[3] salir")
    print("")


def menu():


    print_menu()
    
    opcion = input("Seleccionar opcion: ")

    if opcion == "3":
        print("finalización del programa")
    elif opcion == "1":
        listar_peli()
    elif opcion == "2":
        insertar_peli()
    else:
        print("opción incorrecta")
        menu()

        
#---- Inicio del programa ----

menu()



conexion.close()
