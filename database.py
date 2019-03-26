import pymysql.cursors
import os
connection = pymysql.connect(host='localhost',
                             user = 'root',
                             password='',
                             db='sistema_proyectos',
                             cursorclass=pymysql.cursors.DictCursor   
                            )
def obtener_proyectos():
    try:
        with connection.cursor() as cursor:
            sql = "SELECT `id`,`nombre`,`descripcion`,`responsable` FROM `proyectos`"
            cursor.execute(sql)
            result = cursor.fetchall()
            print("""
ID                      Nombre              Descripcion                                    Responsable
            """)
            #print(result)
            for x in result:
                    print(x['id']," ",x['nombre'], " ", x['descripcion']," ",  x['responsable'], end="\n" )
                   
    finally:
        pass

def obtener_proyecto(id):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT `nombre`,`descripcion`,`responsable` FROM `proyectos` WHERE `id` = %s;"
            cursor.execute(sql,(id))
            result = cursor.fetchall()
            print(result)
    finally:
        pass

def cambiar_nombre(id,nombre):
    os.system("cls")

    try:
        with connection.cursor() as cursor:
            sql = "UPDATE `proyectos` SET `nombre` = %s  WHERE `id` = %s;"
            cursor.execute(sql,(nombre,id))
            connection.commit()
            obtener_proyectos()
             
        

    finally:
        pass
def cambiar_descripcion(id,descripcion):
    os.system("cls")

    try:
        with connection.cursor() as cursor:
            sql = "UPDATE `proyectos` SET `descripcion` = %s  WHERE `id` = %s;"
            cursor.execute(sql,(descripcion,id))
            connection.commit()
            obtener_proyectos()

    finally:
        pass

def cambiar_responsable():
    id = int(input("id: "))
    responsable = input("responsable: ")
    os.system("cls")

    try:
        with connection.cursor() as cursor:
            sql = "UPDATE `proyectos` SET `responsable` = %s  WHERE `id` = %s;"
            cursor.execute(sql,(responsable,id))
            connection.commit()
            obtener_proyectos()

    finally:
            pass
            
def eliminar_proyecto(id):
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM `proyectos` WHERE `id` = %s;"
            cursor.execute(sql,(id))
            connection.commit()
            obtener_proyectos()
    finally:
        pass

