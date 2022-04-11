
from product import Product
# import uuid
# from product import Product

class ProductList:
    ''' Clase que gestiona la lista de productos segun a la clave'''

    ## CONSTRUCTOR PARA LA LISTA DE PRODUCTOS
    def __init__(self):
        self.products = {}
    
    ## AGREGAR PRODUCTO
    def add_product(self, product):
        ''' Agrega un producto a la lista'''
        # id_product = str(uuid.uuid4().hex)  # Generar un identificador único
        self.products[product.id] = product
    
    ## RETORNAR EL PRODUCTO EN ESPECFIICO
    def get_product(self, id):
        ''' Devuelve un producto de la lista'''
        return self.products[id].__json__()

    ## RETORNAR TODA LA LISTA DE PRODUCTOS
    def get_list_products(self):
        ''' Devuelve la lista de productos'''
        list_complete_products = {"products":[]}
        for product in self.products:
            list_complete_products["products"].append(self.products[product].__json__())
        
        # *usado inrtgernamente dict() completo
        # list_complete_products = {}
        # list_complete_products[product] = self.products[product].__json__()
        return list_complete_products
    
    ## ACTUALIZAR PRODUCTO
    def update_product(self,id,product):
        ''' Actualiza un producto de la lista'''
        data_product = self.products[id]
        
        #* actualizando los datos de la clase producto, con los datos del json, no considera los campos que no debe tener y verifica que no se cambie el id
        for key in product:
            if key in data_product.__dict__.keys() and key != "id":
                data_product.__dict__[key] = product[key]

    ## ELIMINAR PRODUCTO
    def delete_product(self,id):
        ''' Elimina un producto de la lista'''
        self.products.pop(id)
        
    def initial_test(self):
        new_product1 = Product("62052123", "Guitarra Eléctrica Squier Bullet Stratocaster HSS con mástil de Laurel - Black", "La Squier Bullet Stratocaster HSS combina estilo, tono y una excelente calidad de construcción, lo que da como resultado un instrumento que se ve y suena bien, pero sigue siendo asequible. Aproveche las mismas imágenes y el tono que aseguraron el lugar de la Stratocaster en la mesa superior del instrumento, todo a un precio más accesible. Un cuerpo elegante y ligero forma la columna vertebral aquí, combinado con un perfil de mástil en forma de C fácil de tocar y un diapasón de laurel. Esto hace que la guitarra sea increíblemente cómoda, permitiéndote practicar y tocar durante horas y horas. Las pastillas de mástil y medio de bobina simple se han combinado con una pastilla de puente humbucker (con conmutación de 5 vías), entregando el icónico sonido Strat que conoces y amas. Un puente de trémolo ayuda a proporcionar efectos adicionales de flexión de cuerdas.", 889.00)

        self.products[new_product1.id] = new_product1
        
        new_product2 = Product("62091283", "Guitarra Acústica FA-115 Dreadnough Pack - Natural", "El nuevo pack de guitarra acústica Fender FA-115 ofrece un excente sonido y un gran valor para cuaquiera que busque comenzar su viaje musical con buen pie e incluye todo lo que necesitas para empezar a tocar: Guitarra Fender FA-115, con cuerpo dreadnought, diapasón Laurel de 20 trastes Puas, correa y cuerdas Funda incluida.", 605.00)

        self.products[new_product2.id] = new_product2
        
