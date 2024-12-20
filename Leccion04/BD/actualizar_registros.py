import psycopg2 # para conectar a postgre

conexion=psycopg2.connect(user = 'postgres',password='Balles1653',host='127.0.0.1',port='5432',database='test_bd')

#print(conexion)


#genero un cursor ,siendo un objeto que nos permite ejecutar sentencias sql 
#recuperamos registros y mas adelante los convertiremos en objetos de python

try:
    with conexion:
        with conexion.cursor() as cursor: 
            sentencia = 'UPDATE  persona SET nombre =%s, apellido =%s, email=%s WHERE id_persona=%s'
            valores=('Juan Carlos','Roldan','rcarlish@sdksk.com',6)#le pasamos los argumentos de cada uno en forma de tupla 
            cursor.execute(sentencia,valores) # utilizamos el metodo executemany 
            registros_actualizados=cursor.rowcount
            print(f'Los registros insertados son: {registros_actualizados}')
        
except Exception as e:
    print(f'Ocurrio un error :{e}')
finally:
    conexion.close()
    
