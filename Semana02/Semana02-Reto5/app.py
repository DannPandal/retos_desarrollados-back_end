
# ! Reto 5: Desarrollar una API para ingresar datos y mostrarlos
# * Desarrollar una API para ingresar los datos (libre) y que por medio de otro endpoint los devuelva.

from flask import Flask,request, jsonify
import uuid

app = Flask(__name__)

data = {}

RESPONSE_ERROR = "Error al procesar la petición"
RESPONSE_ERROR_KEY = "No se encontro el producto con el id ingresado"

@app.route('/')
def welcome():
    return "Bienvenido a la API en Flask datos"

# * GET - devolver todo el contenido
@app.route('/all_data', methods=['GET'])
def all_data():
    try:
        #! jsonify indica el formato de salida application/json
        return jsonify(data)
    except Exception as e:
        return jsonify({"message": RESPONSE_ERROR, "error": str(e)})

# * POST - agregar datos
@app.route('/add_data', methods=['POST'])
def add_data():
    try:
        # * Obtener datos enviados
        data_json = request.get_json()
        data[str(uuid.uuid4())] = data_json
        #! jsonify indica el formato de salida application/json
        return jsonify({"message": "data agregada correctamente"})
    except Exception as e:
        return jsonify({"message": RESPONSE_ERROR, "error": str(e)})


if __name__ == "__main__":
    app.run()



