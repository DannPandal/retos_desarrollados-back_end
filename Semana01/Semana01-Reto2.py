
## ! Reto 2: Personas
from datetime import datetime
from dateutil.relativedelta import relativedelta

# * Hacer un programa que primero capture cuantas Personas vamos a ingresar, luego pedir su nombre, dni y fecha de nacimiento y al final mostrarlas en un orden de la mas joven a la mas adulta

# * Clase Persona
class Person():
    def __init__(self, name, dni, birthday):
        self.name = name
        self.dni = dni
        self.birthday = birthday

    def calculate_age(self):
        #convertir fecha de nacimiento a datetime y asignar la edad 15/04/1998
        self.age = relativedelta(datetime.now(),datetime.strptime(self.birthday, "%d/%m/%Y")).years
    
    def __str__(self):
        return f" * {self.name} tiene {str(self.age)} años." 

    # def __gt__(self, person):
    #     return self.age > person.age


quanity_person = int(input("Ingrese la cantidad de personas a registrar: "))
list_person = []

# * Obtener datos de las personas
for index in range(quanity_person):
    print("\n\nIngresar datos de la persona #" + str(index+1))
    name = input("- Ingrese el nombre de la persona: ")
    dni = input("- Ingrese el dni de la persona: ")
    birthday = input("- Ingrese la fecha de nacimiento de la persona: ")
    newPerson = Person(name, dni, birthday)
    newPerson.calculate_age()
    list_person.append(newPerson)
    #print(x.name + " tiene " + str(x.age) + " años.")

# * impirmiento de datos ordenados
print("\n\nLista de personas ordenadas por edad ")
for item in sorted(list_person, key=lambda x: x.age):
    print(item.__str__())

