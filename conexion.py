import sqlite3



conexion=sqlite3.connect("bd1.db")


try:
    conexion.execute("""create table peliculas (
                              id_peli integer primary key autoincrement,
                              titulo text,
                              direccion text,
                              produccion text,
                              musica text,
                              pais text,
                              anio integer,
                              genero text,
                              sinopsis text
                        )""")
    print("se creo la tabla peliculas")                        
except sqlite3.OperationalError:
    print("La tabla articulos ya existe")                    

#conexion.close()
