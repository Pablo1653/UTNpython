import psycopg2 # para conectar a postgre

conexion=psycopg2.connect(user = 'postgres',password='Balles1653',host='127.0.0.1',port='5432',database='test_bd'
)

#print(conexion)


#genero un cursor ,siendo un objeto que nos permite ejecutar sentencias sql 
#recuperamos registros y mas adelante los convertiremos en objetos de python

try:
    with conexion:
        with conexion.cursor() as cursor: 
            sentencia = 'SELECT * FROM persona where id_persona IN %s' #placeholder es %s 
            entrada=input('Digite los id_persona a buscar (separados por coma): ')
            llaves_primarias=(tuple(entrada.split(',')),)#hacemos una conversion a tupla y cada elemento va separado por , 
            #id_persona=input('Decime que numero de ID queres: ')
            cursor.execute(sentencia,llaves_primarias) # Se ejecuta la sentencia 
            registros=cursor.fetchall()# recupera todos los registros si se usa fetchall que serán una lista pero internamente es una tupla , con fetchone solo uno
            for registro  in registros :
                print(registro)

except Exception as e:
    print(f'Ocurrio un error :{e}')
finally:
    conexion.close()
    
