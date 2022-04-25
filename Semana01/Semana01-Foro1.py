
class Persona():
    def __init__(self,nombre,sexo,apellido,fecha_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.fecha_nacimiento = fecha_nacimiento
    
    def saludar(self):
        return "Hola, soy una persona"

class Profesor(Persona):
    pass
class Alumno(Persona):
    pass

Juan = Profesor("Juan","Herrera","M","15/11/1992")
Dann = Alumno("Dann","Pandal","M","28/07/1991")

print(Juan.nombre)
print(Dann.saludar())
