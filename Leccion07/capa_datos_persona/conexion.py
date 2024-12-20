#objetos de conexion hacia la base de datos:1)cada pool de conexion va a administrar un numero determinados de objetos de conexion hacia la BD 
# la idea es tener disponible en todo momento la conexion de objetos hacia BD : a)un cliente necesita de un objeto de conexion hacia BD , lo obtiene del pool b) una vez que termino su proceso , lo libera y regresa al pool de conexiones para que otro cliente pueda usar un objeto disponible
# dos clientes no pueden usar en el mismo momento el mismo objeto del pool de conexiones  



from psycopg2 import pool
from logger_base import log
import sys

class Conexion:
    _DATABASE = 'test_bd'
    _USERNAME = 'postgres'
    _PASSWORD = 'Balles1653'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtenerConexion(cls):
        if cls._pool is None:
            cls.obtenerPool()
        conexion = cls._pool.getconn()
        log.debug(f'Conexion obtenida del pool: {conexion}')
        return conexion

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON,
                                                      cls._MAX_CON,
                                                      host=cls._HOST,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      port=cls._DB_PORT,
                                                      database=cls._DATABASE)
                log.debug(f'Creacion del pool exitosa: {cls._pool}')
            except Exception as e:
                log.error(f'Ocurrio un error al obtener el pool: {e}')
                sys.exit()
        return cls._pool
    
    @classmethod
    def liberarConexion(cls,conexion):#genera metodo liberar conexion ,recibiendo como argumento el objeto conexion.
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Regresamos la conexión del pool :{conexion}')#cuando un cliente necesita conectarse  a la bd se lo pide al pool , y el pool le regresa un objeto de conexion y una vez que el cliente no usa el objeto se debe llamar al metodo para liberar este objeto y reegresarlo al pool de conexion 
    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerConexion().closeall()


if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
    conexion2 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion2)
    conexion3 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion3)
    conexion4 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion4)
    conexion5 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion5)