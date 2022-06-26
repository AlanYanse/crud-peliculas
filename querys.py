
import conexion

def saludo():
    return "hello from querys"


def insert(titulo, direccion, produccion, musica, pais, anio, genero, sinopsis):

    conexion.conexion.execute("insert into peliculas(titulo ,direccion, produccion, musica, pais, anio, genero, sinopsis) values (?,?,?,?,?,?,?,?)", (titulo, direccion, produccion, musica, pais, anio, genero, sinopsis))


def select_all():

    cursor = conexion.conexion.execute("select * from peliculas")

    for fila in cursor:
        print(fila)





"""
def insert() 


def select()


def delete()


def update()

"""
