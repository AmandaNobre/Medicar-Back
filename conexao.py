import mysql.connector
db_connection = mysql.connector.connect(
    host='localhost', user='root', password='master450', database='medicar')
print('Banco de dados conectado!')