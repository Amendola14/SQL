import sqlite3

miconecxion=sqlite3.connect("garage.db")
mi_cursor= miconecxion.cursor()

#tabla 1 ( movil )

mi_cursor.execute("""
    CREATE TABLE móvil (
    id_movil      INT     PRIMARY KEY
                          NOT NULL
                          UNIQUE,
    patente       VARCHAR NOT NULL
                          UNIQUE,
    marca         VARCHAR NOT NULL,
    modelo        VARCHAR NOT NULL,
    color         VARCHAR NOT NULL,
    observaciones VARCHAR
);
""")

añadir_datos = [
   ("1","4134-ABAS","Ford","1","rojo","nuevo"),
   ("2","53453-AGST","Mercedes","2","verde","nuevo"),
   ("3","857_KJDF","Fiat","3","amarillo","nuevo"),
   ("4","821_ASKD","Honda","4","marron","usado"),
]

mi_cursor.executemany("INSERT INTO móvil VALUES (?,?,?,?,?,?)", añadir_datos)

miconecxion.commit()

#tabla 2 ( movimientos )


mi_cursor.execute("""
    CREATE TABLE movimientos (
    id_movimientos    INT     PRIMARY KEY
                              NOT NULL
                              UNIQUE,
    patente           VARCHAR UNIQUE
                              NOT NULL,
    fechahora_entrada TIME    NOT NULL,
    fechahora_salida  TIME    NOT NULL,
    lugar             VARCHAR NOT NULL
);

""")

añadir_datos = [
    ("1","4134-ABAS","15/06/1215 09:25","16/08/2002 19:55","Balvanera",),
    ("2","53453-AGST","20/12/2022 10:30","02/06/2023 11:11","Barracas"),
    ("3","857-JDF","04/11/2010 10:50","03/12/2010 11:11","Caballito"),
    ("4","821-SKD","10/01/2010 01:43","05/11/2021 20:00","Moreno"),
]

mi_cursor.executemany("INSERT INTO movimientos VALUES (?,?,?,?,?)", añadir_datos)

miconecxion.commit()

#tabla 3 ( usuarios )
mi_cursor.execute("""
    CREATE TABLE usuarios (
    id_usuarios     INT     PRIMARY KEY
                            UNIQUE
                            NOT NULL,
    [nombre
]       VARCHAR NOT NULL,
    user            VARCHAR NOT NULL
                            UNIQUE,
    password        VARCHAR UNIQUE
                            NOT NULL,
    [tipo_usuario ] VARCHAR NOT NULL
);

   
""")

añadir_datos = [
    ("1", "Luis","Luis01239","Lis123","ADMIN"),
    ("2", "Armando","Armando3287","a", "USER"),
    ("3", "Jorge", "JORGE1423","d", "ADMIN"),
    ("4", "Carlos","carlityoxx1342", "f", "USER"),
]

mi_cursor.executemany("INSERT INTO usuarios VALUES (?,?,?,?,?)", añadir_datos)

miconecxion.commit()

miconecxion.close
