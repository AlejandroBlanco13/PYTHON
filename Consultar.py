import mysql.connector
from mysql.connector import Error

def consultar_clientes():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='BD_CLIENTES',
            user='root',
            password='Xiannyale1313.'
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM CLIENTES")
            resultados = cursor.fetchall()
            
            print("IDCLIENTE | NOMBRE | APELLIDOS | EDAD | TELEFONO | EMAIL")
            print("--------------------------------------------------------")
            for row in resultados:
                print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]}")
    
    except Error as e:
        print("Error al conectar a MySQL", e)
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión a MySQL cerrada")

# Ejemplo de uso
consultar_clientes()