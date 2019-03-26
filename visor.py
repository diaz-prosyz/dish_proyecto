import os
def mostrar_menu():
    os.system("cls")
    print ("""
    Seleccione la opcion que desea realizar 
    1.- Ver todos los proyetos
    """)
    respuesta = int(input(">>"))
    return  respuesta
