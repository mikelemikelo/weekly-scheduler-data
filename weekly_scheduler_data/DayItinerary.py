from .task import Task
""" Day itinerary  """

class DayItinerary:

    """ Construct a Scheduled day """
    def __init__(self, for_date):
        self.for_date = for_date
        self.todo_tasks_list = self.load_tasks_by_date(for_date)
        self.completed_tasks_list = []
        self.cancelled_tasks_list = []

    """ Method that returns the associated date for the Scheduled """
    def get_date(self):
        return self.for_date

    """ Method that adds a new task into the associated list of tasks """
    def add_task(self,new_task):
        self.todo_tasks_list.append(new_task)

    """ Method that marks a task as cancelled by task_id """
    def cancel_task(self, task_id):
        for task_iterated in self.tasks_list:
            if task_iterated.task_id == task_id:
                task_iterated.cancelled()

    """ Method that returns the list of TODO tasks """
    def get_todo_task_list(self):
        return self.todo_tasks_list

    """ Method that returns the list of completed tasks """
    def get_completed_task_list(self):
        return self.completed_tasks_list

    """ Method to set the task list """
    def set_task_list(self, task_list):
        for iterated_task in task_list:
            if iterated_task.status == "Completed":
                self.completed_tasks_list.append(iterated_task)
            elif iterated_task.status == "Cancelled":
                self.cancelled_tasks_list.append(iterated_task)
            else:
                self.todo_tasks_list.append(iterated_task)

    """ 
    Method to Load list of tasks for a given input date
    """
    def load_tasks_by_date(self, input_date):
        list_of_tasks = []
        if input_date.weekday() == self.for_date.weekday():
            list_of_tasks.append(Task(None,"Simple", "Predicación", input_date))
            list_of_tasks.append(Task(None, "Simple", "Chess", input_date))

        return list_of_tasks

    """
    Method to mark a given Task as completed, being removed from todo_task_list and appended into completed_task_list.
    """
    def mark_task_as_completed(self, task):
        for iterated_task in self.todo_tasks_list:
            if iterated_task.task_id == task.task_id:
                self.todo_tasks_list.remove(iterated_task)
                task.completed()
                self.completed_tasks_list.append(task)
                break

    """
    Method to mark a given Task as cancelled, being removed from todo_task_list and appended into cancelled_task_list.
    """
    def mark_task_as_cancelled(self,task):
        for iterated_task in self.todo_tasks_list:
            if iterated_task.task_id == task.task_id:
                self.todo_tasks_list.remove(iterated_task)
                task.cancelled()
                self.cancelled_tasks_list.append(task)
                break
