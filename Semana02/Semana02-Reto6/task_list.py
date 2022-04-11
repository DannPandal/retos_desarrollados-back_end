from task import Task


class TaskList:
    ''' Clase que gestiona la lista de productos segun a la clave'''

    ## CONSTRUCTOR PARA LA LISTA DE PRODUCTOS
    def __init__(self):
        self.tasks = {}

    ## AGREGAR TAREA
    def add_task(self, task):    
        self.tasks[task.id] = task

    ## RETORNAR TODA LA LISTA DE PRODUCTOS
    def get_list_tasks(self):
        list_complete_tasks = {"tasks":[]}
        for task in self.tasks:
            list_complete_tasks["tasks"].append(self.tasks[task].__json__())
        return list_complete_tasks

   ## ACTUALIZAR TAREA
    def update_task(self,id,task):
        data_task = self.tasks[id]
        for key in task:
            if key in data_task.__dict__.keys() and key != "id":
                data_task.__dict__[key] = task[key]

    ## ELIMINAR TAREA
    def delete_task(self,id):
        self.tasks.pop(id)

    # CARGA INCIAL DE PRUEBA
    def initial_test(self):
        new_task1 = Task("Primera Tarea", 1)
        self.tasks[new_task1.id] = new_task1
        new_task2 = Task("SEgunda Tarea", 2)
        self.tasks[new_task2.id] = new_task2