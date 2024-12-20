
# importamos nuestra clase de numeros iguales exception
from NumerosIgualesException import NumerosIgualesException

"""
    En otros lenguajes este manejo de excepciones se llama try catch
"""
# genero las variables antes del try

resultado = None
# verificar el resultado que trae sin excepcion
# puedo incluir las variables dentro del bloque y tambien que las ingrese el usuario
a = 10
b = 10

try:
    resultado = a/b
# la renombro en otro objeto como a la excepcion e,la podria nombrar como se me cante
    if a == b:
        # esta palabra "raise" nos permite arrojar una excepcion
        raise NumerosIgualesException('Son números iguales ')
        # arrojamos el msj
except TypeError as e:
    print(f'Ocurrió one error: {type(e)}')
# no seria tan necesario esta excepcion ya que la tomaria la excepcion con la clase padre Exception
except ZeroDivisionError as e:
    print(f'Ocurrió un error : {type(e)}')
# exception es padre de zerodivisionerror
except Exception as e:  # podria ser de zerodivisionerror la clase
    # y no la necesidad de tener en cuenta mas excepciones como la clase padre de exception
    print(f'Ocurrio un error : {type(e)}')

# al final de los bloques except podemos agregar dos bloques mas ,el bloque else y el bloque finally
# el bloque else se ejecutara si no ha lanzado ninguna excepcion
# el bloque else es opcional y se ejecutara solo si no se ejecuto ninguna excepcion
else:
    print("No se arrojo ninguna excepcion")

finally:  # siempre se ejecutara el finally
    print("Ejecucción de este bloque final ")

# como esta fuera del try la variable resultado es none
print(f'El resultado es :{resultado}')

print('seguimos.....')
