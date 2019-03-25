import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user = 'root',
                             password='',
                             db='sistema_proyectos',
                             cursorclass=pymysql.cursors.DictCursor   
                            )

try:
    with connection.cursor() as cursor:
        sql = "SELECT `nombre`,`descripcion`,`responsable` FROM `proyectos`"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()
