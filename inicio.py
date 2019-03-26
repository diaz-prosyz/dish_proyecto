
import subprocess
import os
import administrador
import database

os.system("cls")
print("Bienvenido al sistema de administracion de proyectos")

condicional = 0
intentos = 0
usuario = input("Usuario : ")
contrasena = input("Contraseña : ")


if usuario == "administrador" and contrasena == "123":
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


                    

        if respuesta_menu == 0:
            print(intentos)
            condicional=1
        input("PRESIONE ENTER PARA CONTINUAR") 

else :
    print("El usuario no existe")