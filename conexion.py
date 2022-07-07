import sqlite3



conexion=sqlite3.connect("bd1.db")

cur = conexion.cursor()

try:
    cur.execute("""create table peliculas (
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
    print("La tabla peliculas ya existe")                    

#conexion.close()
