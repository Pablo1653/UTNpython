from Persona import Persona  # Importa el módulo Persona
from conexion import Conexion
from cursor_del_pool import CursorDelPool
from logger_base import log

class PersonaDao:
    """ 
    DAO=Data access object 
    CRUD=create,read,update,delete
    """
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    # Definimos los métodos de clase
    @classmethod
    def seleccionar(cls):
        with CursorDelPool () as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []  # Creamos una lista 
            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[2], registro[3])  # Accedemos a la clase Persona
                personas.append(persona)  # POO
            return personas

    @classmethod
    def insertar(cls,persona):
        with CursorDelPool () as cursor:
            valores=(persona.nombre,persona.apellido,persona.email)
            cursor.execute(cls._INSERTAR,valores)
            log.debug(f'Persona insertada : {persona}')
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls,persona):
        with CursorDelPool () as cursor:
            valores=(persona.nombre,persona.apellido,persona.email,persona.id_persona)
            cursor.execute(cls._ACTUALIZAR,valores)
            log.debug(f'Persona actualizada : {persona}')
            return cursor.rowcount

"""
    @classmethod
    def eliminar(cls,persona):
        with CursorDelPool () as cursor:
            valores=(persona.id_persona,)
            cursor.execute(cls._ELIMINAR,valores)
            log.debug(f'Persona eliminada : {persona}')
            return cursor.rowcount

            
if __name__ == '__main__':
    #Eliminar un registro 
    persona1=Persona(id_persona=86)
    personas_eliminadas=PersonaDao.eliminar(persona1)
    log.debug(f'Personas eliminadas :{personas_eliminadas}')

    #Actualizar un registro
    persona1=Persona(88,'Pertis','Sales','salesperts@sdsd.com')
    personas_actualizadas=PersonaDao.actualizar(persona1)
    log.debug(f'Personas actualizadas:{personas_actualizadas}')

"""

    #insertar un registro
    #persona1=Persona(id_persona='88',nombre='Betty',apellido='Bu',email='BettyBu@hotmail.com')#este objeto es la primer persona
    #personas_insertadas=PersonaDao.insertar(persona1)#generamos una variable
    #log.debug(f'Personas insertadas:{personas_insertadas}')

"""   
    #Seleccionar objetos 
    personas = PersonaDao.seleccionar()
    for persona in personas:
        log.debug(persona)


"""