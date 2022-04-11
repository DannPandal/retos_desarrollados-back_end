

import uuid

"""Clase que representa a una tarea"""

class Task:

    def __init__(self, name, level_priority):
        self.id = str(uuid.uuid4().hex)  # Generar un identificador único
        self.name = name
        self.level_priority = level_priority

    def __gt__(self, task):
        return self.level_priority > task.level_priority

