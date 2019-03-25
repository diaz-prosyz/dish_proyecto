
import subprocess
import os
import administrador
os.system("cls")
print("Bienvenido al sistema de administracion de proyectos")

usuario = input("Usuario : ")
contrasena = input("Contraseña : ")


if usuario == "administrador" and contrasena == "123":
    os.system("cls")
    print("Bienvenido Administrador")
    respuesta = administrador.mostrar_menu()

    if respuesta == 1: 
    	respuesta_mostrar_listado =	administrador.mostrar_listado() 
    	if respuesta_mostrar_listado == 0:
    		administrador.mostrar_menu()
    elif  respuesta == 2:
    	respuesta_editar_proyecto = administrador.editar_proyecto()
    	if respuesta_editar_proyecto == 1:
    		respuesta_editar_campos = administrador.editar_campos()
    		if respuesta_editar_campos == 1:
    			administrador.nuevo_nombre()
				
else :
    print("El usuario no existe")