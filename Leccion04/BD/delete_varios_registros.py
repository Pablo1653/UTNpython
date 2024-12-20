import psycopg2 # para conectar a postgre

conexion=psycopg2.connect(user = 'postgres',password='Balles1653',host='127.0.0.1',port='5432',database='test_bd')



try:
    with conexion:
        with conexion.cursor() as cursor: 
            sentencia='DELETE FROM persona WHERE id_persona IN  %s'
            entrada=input('Digite los numeros de registros a borrar (separados por , )  :')
            valores= (tuple(entrada.split(',')),)#Es una tupla de tuplas
            cursor.execute(sentencia,valores) # utilizamos el metodo execute ya que es un solo registro para modificar 
            registros_eliminados=cursor.rowcount
            print(f'Los registros eliminados son: {registros_eliminados}')
        
except Exception as e:
    print(f'Ocurrió un error :{e}')
finally:
    conexion.close()
