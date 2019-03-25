
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
    administrador.mostrar_menu()

else :
    print("El usuario no existe")