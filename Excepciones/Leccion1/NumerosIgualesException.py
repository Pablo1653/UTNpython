# Aquie estamos generando nuestra propia excepcion #Extiende o hereda  de la clase padre exception
class NumerosIgualesException(Exception):
    def __init__(self, mensaje):
        self.message = mensaje
