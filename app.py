
import conexion
import querys as q

exec(open("conexion.py").read())#auto-ejecuta el fichero conexion.py

#conexion=sqlite3.connect("bd1.db")
"""
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

"""

print("Listar peliculas")

q.select_all()




conexion.close()
