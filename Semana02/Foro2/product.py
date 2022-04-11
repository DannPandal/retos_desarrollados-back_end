
# libreria que permite genere id automatico
import uuid
import json

"""Clase que representa a un producto"""

class Product:

    def __init__(self, code, name, description, price):
        # self.id = uuid.uuid4()
        self.id = str(uuid.uuid4().hex)  # Generar un identificador único
        self.code = code
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"{self.id} - {self.name}, a un precio de S/. {self.price}"

    '''return json format'''
    def __json__(self):
        return {
            "id": self.id,
            "code": self.code,
            "name": self.name,
            "description": self.description,
            "price": self.price
        }
    
    def update_json(self, data_json):
        for key in data_json.keys():
            if key in self.__dict__.keys():
                self.__dict__[key] = data_json[key]
        return self.__dict__
        
    '''return json dumps dict'''
    # def toJSON(self):
    #     ## dumps usado para serealizar un objeto pero sin indicar el tipo de contenido MIME
    #     return json.dumps(self, default=lambda o: o.__dict__, 
    #         sort_keys=True, indent=4)
    