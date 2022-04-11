
# ! Reto 4: Desarrollar una API de mostrar departamentos
# * Desarrollar una API para que nos de la lista de todos los departamentos en el siguiente formato
'''{
  "ok":Boolean,
  "content": List,
  "message": String
}'''
# * en la cual, en el content debe de ir todos los departamentos

from flask import Flask, request, jsonify
import json
import requests

app = Flask(__name__)

# * Clase Persona
RESPONSE_BASE = {
    "ok": False,
    "content": [],
    "message": ""
}

# * bienvenido


@app.route('/')
def welcome():
    return "Bienvenido a la API en Flask departamentos"

# * GET - devolver lista de departamentos de archivo db.json
@app.route('/departamentos_file', methods=['GET'])
def departamentos_file():
    try:
        limpiar_base()
        
        with open("db.json", "r") as file:
            data = json.load(file)
            
            for item in data:
                RESPONSE_BASE["content"].append(item["nombre_ubigeo"])
            RESPONSE_BASE["ok"] = True
            RESPONSE_BASE["message"] = "Respuesta correcta"
      
    except Exception as e:
        RESPONSE_BASE["content"] = []
        RESPONSE_BASE["ok"] = False
        RESPONSE_BASE["message"] = "Error en la consulta, " + str(e)
    finally:
        return jsonify(RESPONSE_BASE)




# # * GET - devolver lista de departamentos de api webapp.inei.gob.pe
@app.route('/departamentos_webapp', methods=['GET'])
def departamentos_webapp():
    try:
        limpiar_base()
        URI = "http://webapp.inei.gob.pe:8080/sisconcode/ubigeo/buscarDepartamentosPorVersion.htm?llaveProyectoPK=5-1"
        response = requests.get(URI)

        if response.status_code == 200:
            data = response.json()
            for item in data:
                RESPONSE_BASE["content"].append( item["descripcion"].replace(item["id"], "").strip() )
            RESPONSE_BASE["ok"] = True
            RESPONSE_BASE["message"] = "Respuesta correcta"
        else:
             raise Exception('API no encontrada, status code: ' + str(response.status_code))

    except Exception as e:
        RESPONSE_BASE["content"] = []
        RESPONSE_BASE["ok"] = False
        RESPONSE_BASE["message"] = "Error en la consulta, " + str(e)
    finally:
        return jsonify(RESPONSE_BASE)


def limpiar_base():
    RESPONSE_BASE["ok"] = False
    RESPONSE_BASE["content"] = []
    RESPONSE_BASE["message"] = ""
