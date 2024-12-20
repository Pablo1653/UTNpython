from logger_base import log


class Persona:#method is a special method that Python calls when a new instance of Persona is created. It takes four arguments#argument is a reference to the current instance of the class and is used to access variables and methods associated with that instance.
    def __init__(self,id_persona,nombre=None,apellido=None,email=None):
        self._id_persona=id_persona#c/u de sus atributos encapsulados 
        self._nombre=nombre
        self._apellido=apellido
        self._email=email

        # Create a new Persona instance
#person = Persona(1, "John", "Doe", "john.doe@example.com")

# Access the instance variables
#print(person._id_persona)  # Output: 1
#print(person._nombre)     # Output: John
#print(person._apellido)   # Output: Doe
#print(person._email)      # Output: john.doe@example.com

    def __str__(self) :

        return f'''
            Id Persona:{self._id_persona},
            Nombre:{self._nombre},
            Apellido:{self._apellido},
            Email:{self._email},

        '''
    
#Métodos getters and setters 

    @property
    def id_persona(self):
        return self._id_persona

    @id_persona.setter
    def id_persona(self,id_persona):
        self._id_persona=id_persona

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,nombre):
        self._nombre=nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self,apellido):
        self._apellido=apellido

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self,email):
        self._email=email


if __name__=='__main__':
    persona1=Persona(1,'Pablito','Sanguuuu','PabliSan@ameria.com')
    persona2=Persona(2,'Anu','Vaz','Vaztun@ameria.com')
    log.debug(persona1)
    log.debug(persona2)