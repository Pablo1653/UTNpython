#el cursor se obtiene de una conexión valida y esta se obtiene del pool
from logger_base import log
from conexion import Conexion



class CursorDelPool:
    def __init__(self):# metodo init 
        self._conexion =None
        self._cursor=None

    def __enter__(self):# metodo enter 
        log.debug('Inicio del metoddo with y __enter__')
        self._conexion=Conexion.obtenerConexion()
        self._cursor=self._conexion.cursor()
        return  self._cursor
    
    def __exit__(self,tipo_exception,valor_exception,detalle_exception):
        log.debug('Se ejecuta el método exit')
        if valor_exception:
            self._conexion.rollback()# si ocurrio un error sale haciend un rollback 
            log.debug(f'Ocurrio una excepción :{valor_exception}')
        else:
            self._conexion.commit()#si no ocurrio ningun error hace un commit 
            log.debug('Commit de la transacción')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)#liberando la conexión 


if __name__=='__main__':
    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque with ')
        cursor.execute('SELECT * FROM persona')
        log.debug(cursor.fetchall())
        