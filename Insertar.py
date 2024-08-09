import mysql.connector
from mysql.connector import Error

def insertar_cliente(nombre, apellidos, edad, telefono, email):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='bd_clientes',
            user='root',
            password='Xiannyale1313.'
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            query = """INSERT INTO CLIENTES (NOMBRE, APELLIDOS, EDAD, TELEFONO, EMAIL)
                       VALUES (%s, %s, %s, %s, %s)"""
            record = (nombre, apellidos, edad, telefono, email)
            cursor.execute(query, record)
            connection.commit()
            print("Cliente insertado exitosamente")
    
    except Error as e:
        print("Error al conectar a MySQL", e)
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión a MySQL cerrada")

# Ejemplo de uso
insertar_cliente('Juan', 'Pérez', 30, '1234567890', 'juan.perez@example.com')
