import logging as log 

# Llamamos una configuración básica

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s:%(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p' ,
                handlers=[
                    log.FileHandler('capa datos.log'),
                    log.StreamHandler()
                ])#%s es el parametro posicional #datefmt =date format 


if __name__ == '__main__' :
    

    log.debug('Mensaje a nivel debug ')

    log.info('Mensaje a nivel info')

    log.warning('Mensaje a nivel warning ')

    log.error('Mensaje a nivel error ')

    log.critical('Mensaje a nivel critical')



