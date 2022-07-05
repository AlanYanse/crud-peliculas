
import conexion

def saludo():
    return "hello from querys"


def insert(titulo, direccion, produccion, musica, pais, anio, genero, sinopsis):

    conexion.cur.execute("insert into peliculas(titulo ,direccion, produccion, musica, pais, anio, genero, sinopsis) values (?,?,?,?,?,?,?,?)", (titulo, direccion, produccion, musica, pais, anio, genero, sinopsis))

    conexion.conexion.commit()


def select_all():
    for row in conexion.cur.execute('SELECT * FROM peliculas'):
        print(row)

"""

def delete()


def update()

"""
