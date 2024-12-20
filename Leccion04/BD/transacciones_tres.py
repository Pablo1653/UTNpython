import psycopg2 as  bd # para conectar a postgre#renombrado con un alias 
#una transacción puede leer una o mas sentencias que modifiquen el estado de la BD  
conexion=bd.connect(user = 'postgres',password='Balles1653',host='127.0.0.1',port='5432',database='test_bd')

#print(conexion)


#genero un cursor ,siendo un objeto que nos permite ejecutar sentencias sql 
#recuperamos registros y mas adelante los convertiremos en objetos de python

try:
#no vamos a utilizar with ya que guarda automaticamente en la BD y si hay un error hace un rollback automaticamente , por eso lo hacemos de forma manual
    with conexion:
        with conexion.cursor() as cursor:
            sentencia= 'INSERT INTO persona (nombre,apellido,email) VALUES (%s,%s,%s)'
            valores=('Richardios','Fortunatio','forturi@hotmail.com')
            cursor.execute(sentencia,valores)

            sentencia= 'UPDATE persona SET nombre=%s , apellido=%s ,email=%s  WHERE  id_persona=%s' #en esta sentencia actualiza un valor 
            valores =('Marche','Herbie','herbie66@gmail.com',5)#tupla de valores 
            cursor.execute(sentencia,valores) # incorporamos un execute para incorporar la sentencia y los valores a esta ejecución 
            
            
except Exception as e:
    #hace el rollback automaticamente y no necesita que lo estemos ejecutando
    print(f'Ocurrio un error,se hizo un rollback {e}')
finally:
    conexion.close()

print('Termina la transacción ')
