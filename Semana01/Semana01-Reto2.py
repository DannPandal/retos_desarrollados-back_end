
## ! Reto 2: Personas

# * Hacer un programa que primero capture cuantas Personas vamos a ingresar, luego pedir su nombre, dni y fecha de nacimiento y al final mostrarlas en un orden de la mas joven a la mas adulta

class Person():
    def __init__(self, name, dni, birthday):
        self.name = name
        self.dni = dni
        self.birthday = birthday

    def saludar(self):
        return "Hola, soy una persona"

quanity_person = int(input("Ingrese la cantidad de personas a registrar:"))
list_person = []


