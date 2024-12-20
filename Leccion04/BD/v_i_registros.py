import psycopg2 # para conectar a postgre

conexion=psycopg2.connect(user = 'postgres',password='Balles1653',host='127.0.0.1',port='5432',database='test_bd')

#print(conexion)


#genero un cursor ,siendo un objeto que nos permite ejecutar sentencias sql 
#recuperamos registros y mas adelante los convertiremos en objetos de python

try:
    with conexion:
        with conexion.cursor() as cursor: 
            sentencia = 'INSERT INTO persona (nombre,apellido,email) VALUES (%s,%s,%s)'
            valores=(
                ('Carlos','Larson','clara@fjksd.com'),
                ('Marcos','Rojo','yacobiti@america.com'),
                ('Marcelita','Cuenca','craneviter@yahoo.com')
                )#Es una tupla de tuplas 
            cursor.executemany(sentencia,valores) # utilizamos el metodo executemany 
            #conexion.commit() este se utilizaria para guardar los cambios en la bd pero al tener with ya lo hace automatico .#se hace un roll back  si en el error se quiere volver atras
            registros_insertados=cursor.rowcount
            print(f'Los registros insertados son: {registros_insertados}')
        
except Exception as e:
    print(f'Ocurrio un error :{e}')
finally:
    conexion.close()
    
