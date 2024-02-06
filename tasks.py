class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def delete_task(self, index):
        del self.tasks[index]

    def complete_task(self, index):
        self.tasks[index].completed = True

    def get_task_list(self):
        return self.tasks
