class Pelicula:

    # método __init__ de la biblioteca Thunder
    def __init__(self, nombre):
        self._nombre = nombre

    def __str__(self):
        return f'Pelicula: {self._nombre}'

    @property  # metodo get
    def nombre(self):
        return self._nombre

    @nombre.setter  # metodo setter
    def nombre(self, nombre):
        self._nombre = nombre
