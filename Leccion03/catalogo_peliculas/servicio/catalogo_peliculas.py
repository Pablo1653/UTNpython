import os  # importa desde sistema operativo, lo voy a utilizar el metodo remove


class CatalogoPeliculas:

    # atributo de clase
    ruta_archivo = 'peliculas.txt'

    # metodo de clase ,que accede a los atributos de clase por eso utiliza ese decorator
    # 1 opcion
    @classmethod
    # agregamos contexto de clase cls en lugar de self que se usa en instancia
    # es decir cls es decir recibe la propia clase como primer parametro
    def agregar_peliculas(cls, pelicula):
        # le pasamos parametro pelicula
        with open(cls.ruta_archivo, 'a', encoding='utf8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')

    # 2 opcion
    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo, 'r', encoding='utf8') as archivo:
            print(f'Catalogo de peliculas'.center(50, '-'))
            print(archivo.read())

    # 3 pelicula
    @classmethod
    def eliminar_peliculas(cls):
        os.remove(cls.ruta_archivo)
        print(f'Archivo eliminado:{cls.ruta_archivo}')
