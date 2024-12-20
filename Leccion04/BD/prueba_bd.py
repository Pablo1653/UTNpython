import psycopg2 # para conectar a postgre

conexion=psycopg2.connect(user = 'postgres',password='Balles1653',host='127.0.0.1',port='5432',database='test_bd')

#print(conexion)


#genero un cursor ,siendo un objeto que nos permite ejecutar sentencias sql 
#recuperamos registros y mas adelante los convertiremos en objetos de python

try:
    with conexion:
        with conexion.cursor() as cursor: 
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s' #placeholder es %s #Aca de puede poner la query que desees  
            id_persona = input('Decime que numero de ID queres: ')
            cursor.execute(sentencia , (id_persona,)) # Se ejecuta la sentencia 
            registros= cursor.fetchone()# recupera todos los registros si se usa fetchall que serán una lista pero internamente es una tupla , con fetchone solo uno
            print(registros)

except Exception as e:
    print(f'Ocurrio un error :{e}')
finally:
    conexion.close()


