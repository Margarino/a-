import pymysql
from RegionClass import Region

def connect():
    try:
        conexion = pymysql.connect(host = 'localhost', user = 'root', password='',db='rapey')
    except:
        print("Problemas al conectar")
    return conexion

def insert(Region):
    conexion = connect()
    try:
        with conexion.cursor() as cursor:
            sql = "INSERT INTO Region (Nombre, Nro_region) VALUES (%s,%s);"
            cursor.execute(sql,(Region.Nombre,Region.Nro_region))
        conexion.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Error al insertar en la base de datos: ",e)
    conexion.close()

def update(Region):
    conexion = connect()
    try:
        with conexion.cursor() as cursor:
            sql = "UPDATE Region SET Nombre = %s where Nro_region = %s;"
            cursor.execute(sql,(Region.Nombre,Region.Nro_region))
        conexion.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Error al modificar en la base de datos: ",e)
    conexion.close()

def delete(Nro_region):
    conexion = connect()   
    try:
        with conexion.cursor() as cursor:
            sql = "DELETE FROM Region where Nro_region = %s;"
            cursor.execute(sql,(Nro_region))
        conexion.commit
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Error al eliminar de la base de datos: ",e)
    conexion.close()

def query():
    conexion = connect()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT Nombre, Nro_region from region;") 
            auxRegion = cursor.fetchall()
        return auxRegion
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Error al consultar la base de datos: ",e)
    conexion.close()

def search (Nro_region):
    conexion = connect()
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT * FROM Region WHERE Nro_region = %s;"
            cursor.execute(sql,(Nro_region))
            auxRegion = cursor.fetchall()
            return auxRegion
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Error al buscar en la base de datos:",e)
    conexion.close()