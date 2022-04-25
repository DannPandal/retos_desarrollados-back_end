
# ! Reto 3: Desarrollo de Productos con POO

# *Tener un programa que reciba una cantidad de productos a ingresar, que luego de ingresarlos (instanciar) podamos llamar a uno de ellos y que nos muestre su descripción y si no, tengamos una opción para terminar el programa. (Usar if elif else y while)

class product():
    def __init__(self, code, description, price):
        self.code = code
        self.description = description
        self.price = price

    def __str__(self):
        return f"{self.code} - {self.description}, a un precio de S/. {self.price}"


quanity_product = int(input("Ingrese la cantidad de productos a registrar: "))
list_product = []

## ingreso de productos
for index in range(quanity_product):
    print("\n\nIngresar datos del producto #" + str(index+1))
    code = input("- Ingrese el codigo del producto: ")
    description = input("- Ingrese la descripcion del producto: ")
    price = float(input("- Ingrese el precio del producto: "))
    newProduct = product(code, description, price)
    list_product.append(newProduct)

## imprimir producto indicado por codigo
validate = True
while validate:
    search_validate = True
    code = input("\n\nIngrese el codigo del producto que busca: ")
    for item in list_product:
        if item.code == code:
            print(f"El producto es {item.__str__()}")
            search_validate = False
            validate = False
            break
    if search_validate:
        print("\n\nEl codigo ingresado no existe, desea ingresar otro codigo? (si/no)")
        answer = input()
        if answer == "si":
            validate = True
        else:
            validate = False

