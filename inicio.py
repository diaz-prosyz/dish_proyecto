
import subprocess
import os
os.system("cls")
print("Bienvenido al sistema de administracion de proyectos")

usuario = input("¿Cual es tu usuario : ?")
contrasena = input("¿Cual es tu contraseña : ?")

if usuario == "administrador" and contrasena == "123":
    os.system("cls")
    print("Bienvenido Administrador")
else :
    print("El usuario no existe")