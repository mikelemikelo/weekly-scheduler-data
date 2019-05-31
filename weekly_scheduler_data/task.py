import uuid
""" Task abstract class definition """


class Task:

    """ Task statuses: Created - Completed - Cancelled """
    def __init__(self, task_id, task_type, name, due_date):
        """ Create a new task """
        if task_id is None:
            self.task_id = str(uuid.uuid4())
        else:
            self.task_id = task_id

        self.task_type = task_type
        self.name = name
        self.due_date = due_date
        self.status = "Created"

    """ Method to complete a task """
    def completed(self):
        self.status = "Completed"

    """ Method to cancel a task """
    def cancelled(self):
        self.status = "Cancelled"

    """ to_json() method overwritten """
    def to_json(self):
        return {
            "task_id": self.task_id,
            "task_type": self.task_type,
            "name": self.name,
            "due_date": self.due_date,
            "status": self.status
        }