class TaskTracker():

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "status": "to do"}
        )
    
    def list_todo(self):
        return [task['task'] for task in self.tasks]
    
    def mark_complete(self, task):

        for item in self.tasks:
            if item['task'] == task:
                item['status'] = 'complete'

 