import os
import database


def mostrar_menu():
    os.system("cls")
    print ("""
    Seleccione la opcion que desea realizar 
    1.- Ver todos los proyetos
    2.- Editar un proyecto 
    3.- Eliminar un proyecto 
    4.- Crear un proyecto 
    5.- Ver informacion de una API publica 
    """)
    respuesta = int(input(">>"))
    return  respuesta

def mostrar_listado_proyectos(): 
	os.system("cls")
	database.obtener_proyectos()
	print("\n")
	print (" Volver al menu. Presione 0 ")
	respuesta = int(input(">>"))
	return respuesta

def editar_proyecto():
	os.system("cls")
	database.obtener_proyectos()
	respuesta = int(input(">>"))
	return respuesta

def editar_campos():
	os.system("cls")
	print("""
	
		¿Que campo desea editar?

		1.-Nombre
		2.-Descripcion 
		3.-Responsable 

		""")
	respuesta = int(input(">>"))
	return respuesta

def nuevo_nombre():
	os.system("cls")
	print("""
		Ingrese un nombre. Presione Enter para guardar

		""")	
	respuesta = input(" Nuevo Nombre: ")
	print (" Volver al menu. Presione 0 ")
	return respuesta
	

def nueva_descripcion():
	os.system("cls")
	print("""
		Ingrese nueva descripcion. Presione Enter para guardar
	
	""")
	respuesta = input(" Nueva Descripcion: ")
	print (" Volver al menu. Presione 0 ")
	return respuesta

def nuevo_responsable():
	os.system("cls")
	print("""
		Ingrese responsable. Presione Enter para guardar
	
	""")
	respuesta = input(" Nuevo Responsable: ")
	print (" Volver al menu. Presione 0 ")
	return respuesta

	
	