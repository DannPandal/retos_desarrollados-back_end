
# ! Reto 5: Desarrollar una API para ingresar datos y mostrarlos
# * Desarrollar una API para ingresar los datos (libre) y que por medio de otro endpoint los devuelva.

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Bienvenido a la API en Flask datos"





