import pymysql
from RestaurantClass import Restaurant

def connect():
    try:
        conexion = pymysql.connect(host = 'localhost', user = 'root', password='',db='rapey')
    except:
        print("Problemas al conectar")
    return conexion

def insert(Restaurant):
    conexion = connect()
    try:
        with conexion.cursor() as cursor:
            sql = "INSERT INTO Restaurant (Nombre, Id_restaurant, Id_comida, Nro_region) VALUES(%s,%s,%s,%s);"
            cursor.execute(sql,(Restaurant.Nombre, Restaurant.Id_restaurant, Restaurant.Id_comida, Restaurant.Nro_region))
        conexion.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Error al insertar en la base de datos: ",e)
    conexion.close()

def update(Restaurant):
    conexion = connect()
    try:
        with conexion.cursor() as cursor:
            sql = "UPDATE Restaurant SET Nombre = %s, Id_comida = %s, Nro_region = %s where Id_restaurant = %s;"
            cursor.execute(sql,(Restaurant.Nombre, Restaurant.Id_comida, Restaurant.Nro_region, Restaurant.Id_restaurant))
            conexion.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Error al modificar en la base de datos: ",e)
    conexion.close()

def delete (Id_restaurant):
    conexion = connect()
    try:
        with conexion.cursor() as cursor:
            sql = "DELETE FROM Restaurant where Id_restaurant = %s;"
            cursor.execute(sql,(Id_restaurant))
        conexion.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Error al eliminar de la base de datos: ",e)
    conexion.close()

def query():
    conexion = connect()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT Nombre, Id_restaurant, Id_comida, Nro_region from Restaurant;")
            auxRestaurant = cursor.fetchall()
        return auxRestaurant
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Error al consultar la base de datos: ",e)
    conexion.close()

def search(Id_restaurant):
    conexion = connect()
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT * FROM Restaurant where Id_restaurant = %s;"
            cursor.execute(sql,(Id_restaurant))
            auxRestaurant = cursor.fetchall()
            return auxRestaurant
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Error al buscar en la base de datos:",e)
    conexion.close()