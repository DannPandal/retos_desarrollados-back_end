
# ! API REST FLASK
'''generar una API sencilla en la cual usemos los verbos HTTP (GET, POST, PUT, DELETE) para poder modificar una lista de datos (puede ser una lista de productos por ejemplo).'''

from flask import Flask, request, jsonify
from product import Product
from product_list import ProductList

app = Flask(__name__)


RESPONSE_ERROR = "Error al procesar la petición"
RESPONSE_ERROR_KEY = "No se encontro el producto con el id ingresado"

#* carga inicial de datos, para pruebas
products_list = ProductList()
products_list.initial_test()


# * bienvenido
@app.route('/')
def welcome():
    return "Bienvenido a la API en Flask de productos"

# * GET - devolver lista de productos


@app.route('/all_product', methods=['GET'])
def list_product():
    try:
        #! jsonify indica el formato de salida application/json
        return jsonify(products_list.get_list_products())
    except Exception as e:
        return jsonify({"message": RESPONSE_ERROR, "error": str(e)})


# * POST - agregar producto a lista de productos
@app.route('/add_product', methods=['POST'])
def add_product():
    try:
        # * Obtener datos enviados
        data_json = request.get_json()
        # * Crear objeto producto
        new_product = Product(
            data_json["code"], data_json["name"], data_json["description"], data_json["price"])
        # * Agregar producto a lista
        products_list.add_product(new_product)
        # * Devolver lista de productos
        #! jsonify indica el formato de salida application/json
        return jsonify(products_list.get_list_products())
    except Exception as e:
        return jsonify({"message": RESPONSE_ERROR, "error": str(e)})


# * PUT - actualizar producto de lista de productos
@app.route('/update_product/<string:id>', methods=['PUT'])
def update_task(id):
    try:
        data_json = request.get_json()
        products_list.update_product(id, data_json)
        return jsonify(products_list.get_list_products())
    except KeyError:
        return jsonify({"message": RESPONSE_ERROR_KEY})
    except Exception as e:
        return jsonify({"message": RESPONSE_ERROR, "error": str(e)})


# * DELETE - borrar producto de lista de productos
@app.route('/delete_product/<string:id>', methods=['DELETE'])
def delete_product(id):
    try:
        products_list.delete_product(id)
        return jsonify(products_list.get_list_products())
    except KeyError:
        return jsonify({"message": RESPONSE_ERROR_KEY})
    except Exception as e:
        return jsonify({"message": RESPONSE_ERROR, "error": str(e)})


if __name__ == "__main__":
    app.run()
#     app.run(host='0.0.0.0',
#             debug=True,
#             port=8080)
