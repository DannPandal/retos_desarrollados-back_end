
# ! Reto 6: Desarrollar una API para mostrar tareas pendientes
# * Para este reto deberemos de crear una API en la cual ingresemos una tarea y su prioridad y que nos muestre la lista de tareas con sus prioridades y la opción de poder actualizarla mediante su ID y eliminarla también mediante su ID.

from ssl import ALERT_DESCRIPTION_ACCESS_DENIED
from flask import Flask,request, jsonify
from task import Task
from task_list import TaskList

app = Flask(__name__)


RESPONSE_ERROR = "Error al procesar la petición"
RESPONSE_ERROR_KEY = "No se encontro el producto con el id ingresado"

#* carga inicial de datos, para pruebas
task_list_dict = TaskList()
task_list_dict.initial_test()


# * bienvenido
@app.route('/')
def welcome():
    return "Bienvenido a la API en Flask de prioridad de Tareas"

# * GET - devolver lista de tareas
@app.route('/all_task', methods=['GET'])
def all_task():
    try:
        return jsonify(task_list_dict.get_list_tasks() )
    except Exception as e:
        return jsonify({"message": RESPONSE_ERROR, "error": str(e)})


# * POST - agregar producto a lista de productos
@app.route('/add_task', methods=['POST'])
def add_task():
    try:
        data_json = request.get_json()
        new_task = Task(
            data_json["name"], data_json["level_priority"])
        task_list_dict.add_task(new_task)
        return jsonify(task_list_dict.get_list_tasks())
    except Exception as e:
        return jsonify({"message": RESPONSE_ERROR, "error": str(e)})

# * PUT - actualizar task de lista de productos
@app.route('/update_task/<string:id>', methods=['PUT'])
def update_task(id):
    try:
        data_json = request.get_json()
        task_list_dict.update_task(id, data_json)
        return jsonify(task_list_dict.get_list_tasks())
    except KeyError:
        return jsonify({"message": RESPONSE_ERROR_KEY})
    except Exception as e:
        return jsonify({"message": RESPONSE_ERROR, "error": str(e)})


# * DELETE - borrar producto de lista de productos
@app.route('/delete_task/<string:id>', methods=['DELETE'])
def delete_task(id):
    try:
        task_list_dict.delete_task(id)
        return jsonify(task_list_dict.get_list_tasks())
    except KeyError:
        return jsonify({"message": RESPONSE_ERROR_KEY})
    except Exception as e:
        return jsonify({"message": RESPONSE_ERROR, "error": str(e)})


if __name__ == "__main__":
    app.run()
