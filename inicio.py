
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
    	respuesta_mostrar_listado_proyectos =	administrador.mostrar_listado_proyectos() 

else :
    print("El usuario no existe")