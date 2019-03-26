
import subprocess
import os
import administrador
import database
import requests
import visor
from tabulate import tabulate

os.system("cls")
print("Bienvenido al sistema de administracion de proyectos")

condicional = 0
intentos = 0
usuario = input("Usuario : ")
contrasena = input("Contraseña : ")
validacion = database.validar_usuario(usuario,contrasena)
tipo_usuario = validacion
tipo_usuario = tipo_usuario[0]["rol"]

if tipo_usuario == 0: #Adminsitrador
    if validacion:
        os.system("cls")
        print("Bienvenido Administrador")
        while condicional == 0:
            intentos +=1
            respuesta_menu  = administrador.mostrar_menu()
            
            if respuesta_menu == 1:
                    administrador.mostrar_listado_proyectos()
            if respuesta_menu == 2:
                    id_editar_proyecto = administrador.editar_proyecto()
                    os.system("cls")
                    opcion_editar_campos = administrador.editar_campos()
                    if opcion_editar_campos == 1:
                        respuesta_nuevo_nombre = administrador.nuevo_nombre()
                        database.cambiar_nombre(id_editar_proyecto,respuesta_nuevo_nombre)
                    if opcion_editar_campos == 2:
                        respuesta_nueva_descripcion = administrador.nueva_descripcion()
                        database.cambiar_descripcion(id_editar_proyecto,respuesta_nueva_descripcion)
                    if opcion_editar_campos == 3:
                        respuesta_nueva_responsable = administrador.nuevo_responsable()
                        database.cambiar_responsable(id_editar_proyecto,respuesta_nueva_responsable)

            if respuesta_menu == 3:#eliminar el proyecto
                print("Seleccione el proyecto a eliminar.")
                id_eliminar_proyecto = administrador.mostrar_listado_proyectos()
                database.eliminar_proyecto(id_eliminar_proyecto)
            
            if respuesta_menu == 4: #Crear proyecto
                os.system("cls")
                print("Formulario de creación de proyectos.Presione enter para guardar cada campo requerido")
                nombre = input("Dame el nombre del proyecto: ")
                descripcion = input("Dame la descripcion: ")
                responsable = input("Dame el responsable: ")

                database.crear_proyecto(nombre,descripcion,responsable)
            if respuesta_menu == 5: #Traer informacion de una API
                data = []
                os.system("cls")
                print("Esta informacion viene de paginas del gobierno de la ciudad de México")
                informacion = requests.get('https://jsonplaceholder.typicode.com/posts')
                resultado = informacion.json()
                resultado = resultado[:10]
                for x in resultado:
                    print(" El titulo del post es : ", x['title']) 
            if respuesta_menu == 6:
                print("Formulario de creacion de usuario.")
                
                usuario = input("Dame el usuario: ")
                contrasenia = input("Dame el contraseña: ")
                rol = int(input("Dame el tipo de usuario 1=Visor y 0= Administrador: "))
                database.crear_usuario(usuario,contrasenia,rol)
                    
                
                
                
                


                        

            if respuesta_menu == 0:
                print(intentos)
                condicional=1
            input("PRESIONE ENTER PARA CONTINUAR") 

    else :
        print("El usuario no existe")
else:
    while condicional == 0 :
        os.system("cls")
        database.obtener_proyectos()
        proyecto_seleccionado = int(input("Selecciona el ID del proyecto especifico o 0 para salir: "))
        if proyecto_seleccionado == 0:
            exit()
        os.system("cls")
        database.obtener_proyecto(proyecto_seleccionado)
        print("Selecciona 0 para salir")

    
    