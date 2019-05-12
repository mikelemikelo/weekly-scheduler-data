import uuid
""" Task abstract class definition """


class Task:

    """ Task statuses: Created - Completed - Cancelled """
    def __init__(self, task_id, task_type, name, due_date):
        """ Create a new task """
        if task_id is None:
            self.task_id = uuid.uuid4()
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