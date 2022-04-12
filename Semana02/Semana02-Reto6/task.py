
import uuid

"""Clase que representa a una tarea"""

class Task:

    def __init__(self, name, level_priority):
        self.id = str(uuid.uuid4().hex)  # Generar un identificador único
        self.name = name
        self.level_priority = level_priority

    def __gt__(self, task):
        return self.level_priority > task.level_priority

    def __json__(self):
        return {
            "id": self.id,
            "name": self.name,
            "level_priority": self.level_priority
        }

    def update_json(self, data_json):
        for key in data_json.keys():
            if key in self.__dict__.keys():
                self.__dict__[key] = data_json[key]
        return self.__dict__

