import pymysql.cursors

connection=pymysql.connect(host='localhost', user='root', password='', db='flash_store', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

try:
	
	with connection.cursor() as cursor:
		sql="SELECT NOMBRE, APELLIDO, USUARIO, PERFIL FROM usuarios WHERE ID=%s"
		cursor.execute(sql, ('1'))
		result=cursor.fetchone()
		print(result)

finally:
	connection.close()