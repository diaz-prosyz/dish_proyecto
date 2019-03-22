"""
     Proyecto:
	Descripción:
		Dado que el interés es demostrar el conocimiento del lenguaje Python y bases de datos (básico) más que el dominio de la parte web con frameworks como Django, el proyecto consiste en una aplicación interactiva de consola.
		El proyecto consiste a grandes rasgos en realizar un CRUD (Create, Read, Update and Delete) o ABC (Alta, Baja y Cambio).
		El proyecto simula un portafolio de proyectos.
		El proyecto incluye el consumo de alguna API REST de libre uso.
	
	Necesidades:
		1.1- Que se pueda observar una lista de proyectos, su descripción y algunas propiedades del mismo, como "Project Manager encargado", "Desarrolladores involucrados", etc. (se pueden incluir tantas propiedades como se desee).
		1.2.- La aplicación requiere 2 usuaris, uno del tipo "administrador", que pueda ver, modificar, agregar y borrar algún proyecyo del listado (el CRUD completo) y uno de tipo "visor", que pueda ver el listado de proyectos e, introduciendo el número o identificador del proyecto, pueda ver los detalles de cada uno (sólo la R del CRUD).
		2.1.- Además de la sección del portafolio de proyectos, se debe poder visualizar llamadas a algún servicio REST de libre uso y mostrar los datos que arroja dicho servicio, no es necesario algún formato en especial, sólo no imprimir en JSON directamente.

	Requisitos de herramientas:
		1- Python 3.6 o superior.
		2- Instalaciones mediante pip.
		3- Se puede usar tanto Python plano para realizar consultas a BD, así como helper o bibliotecas, siempre y cuando permitan hacer la manipulación de queries directamente por el desarrollador, es decir, que no lo construyan interamente. De preferencia, se debe hacer uso de los patrones DAO-DTO, así como de Singleton.
		4- Para REST se puede utilizar tanto Python plano, así como Unirest.
		5- Se debe entregar una implementación con el motor de Oracle (en su versión libre para este proyecto), entregar además una implementación con el motor MySQL es un plus (incluir qué archivos excluir y qué dependencias no instalar cuando se trate de un motor u otro).
		* Se puede hacer uso del paradigma que sea, aunque será un plus hacerlo orientado a objetos.
	
	Requisitos de entrega:
		1- Entregar proyecto en un repositorio público de algún sistema compatible con Git (Github, Gitlab, CodeCommit, etc.) o, en su defecto, un comprimido por correo a rogelio.ramirez@dish.com.mx
		2- Incluir instrucciones (Word .doc o .docx con imágenes) para cargar la base de datos, instalar dependencias y ejecutar el proyecto (incluir script de base de datos y comandos para las dependencias).
		3- Incluir instrucciones (Word .doc o .docx con imágenes) para hacer un recorrido completo del proyecto ejecutándose.
		4- El proyecto debe contener el código documentado a nivel de clases/archivo, métodos publicos/funciones y rutinas complejas (en caso de existir). Se puede dcocumentar con comentarios normales o con PyDoc.

"""
import subprocess
import os
os.system("cls")
print("""Bienvenido al sistema de portafolio de proyectos

    ¿Que deseas realizar?

    1-Ver listado de proyectos
    2-Ver información de una API
""")