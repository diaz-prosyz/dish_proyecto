import pymysql.cursors # Libreria de conexion con mysql
import os
from tabulate import tabulate # Libreria de creacion de tablas
connection = pymysql.connect(host='localhost',
                             user = 'root',
                             password='',
                             db='sistema_proyectos',
                             cursorclass=pymysql.cursors.DictCursor   
                            )
def obtener_proyectos():  # Se obtienen todos los proyectos
    try:
        with connection.cursor() as cursor:
            sql = "SELECT `id`,`nombre`,`descripcion`,`responsable` FROM `proyectos`"
            cursor.execute(sql)
            result = cursor.fetchall()
            #print(result)
            ##for x in result:
              ##      print(x['id']," ",x['nombre'], " ", x['descripcion']," ",  x['responsable'], end="\n" )
            print(tabulate(result))
                   
    finally:
        pass

def obtener_proyecto(id): # Se obtiene un proyecto
    try:
        with connection.cursor() as cursor:
            sql = "SELECT `nombre`,`descripcion`,`responsable` FROM `proyectos` WHERE `id` = %s;"
            cursor.execute(sql,(id))
            result = cursor.fetchall()
            print(tabulate(result))
            input("")
    finally:
        pass

def cambiar_nombre(id,nombre): # Cambiar nombre en la base de datos
    os.system("cls")

    try:
        with connection.cursor() as cursor:
            sql = "UPDATE `proyectos` SET `nombre` = %s  WHERE `id` = %s;"
            cursor.execute(sql,(nombre,id))
            connection.commit()
            obtener_proyectos()
             
        

    finally:
        pass
def cambiar_descripcion(id,descripcion): # Cambiar descripcion en la base de datos
    os.system("cls")

    try:
        with connection.cursor() as cursor:
            sql = "UPDATE `proyectos` SET `descripcion` = %s  WHERE `id` = %s;"
            cursor.execute(sql,(descripcion,id))
            connection.commit()
            obtener_proyectos()

    finally:
        pass

def cambiar_responsable(id,responsable): # Cambiar responsable en la base de datos
    os.system("cls")

    try:
        with connection.cursor() as cursor:
            sql = "UPDATE `proyectos` SET `responsable` = %s  WHERE `id` = %s;"
            cursor.execute(sql,(responsable,id))
            connection.commit()
            obtener_proyectos()

    finally:
            pass

def crear_proyecto(nombre, descripcion, responsable): # Se puede crear proyectos
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO proyectos (nombre, descripcion, responsable) VALUES(%s,%s,%s)"
            cursor.execute(sql,(nombre,descripcion,responsable))
            connection.commit()
            os.system("cls")
            obtener_proyectos()
    finally:
        pass
def crear_usuario(usuario, contrasenia, rol): # crear usuario en la base de datos
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO usuarios (usuario, contrasenia, rol) VALUES(%s,%s,%s)"
            cursor.execute(sql,(usuario,contrasenia,rol))
            connection.commit()
            print("Se ha creado el usuario con exito")
            input("ENTER para continuar.")
            os.system("cls")

    finally:
        pass
def eliminar_proyecto(id): # Eliminar el proyecto
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM `proyectos` WHERE `id` = %s;"
            cursor.execute(sql,(id))
            connection.commit()
            obtener_proyectos()
    finally:
        pass

def validar_usuario(usuario,contrasenia): # Validacion de login
    os.system("cls")
    try:
        with connection.cursor() as cursor:
            sql = "SELECT `usuario`,`contrasenia`,`rol`   FROM `usuarios` WHERE `usuario` = %s AND `contrasenia` = %s ;"
            cursor.execute(sql,(usuario,contrasenia))
            result = cursor.fetchall()
            if result:
                return result
            else: 
                return False
    finally:
        pass
