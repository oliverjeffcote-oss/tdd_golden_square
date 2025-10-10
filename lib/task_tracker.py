class TaskTracker():

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.validate_input(task)
        self.tasks.append({"task": task, "status": "to do"}
        )
    
    def list_todo(self):
        return [task['task'] for task in self.tasks if task['status'] == "to do"]
    
    def mark_complete(self, task):
        self.validate_input(task)

        for item in self.tasks:
            if item['task'] == task:
                if item['status'] == 'complete':
                    return "Task is already completed."
                else:
                    item['status'] = 'complete'
                    return
        
        raise Exception("Task not found.")

    def validate_input(self, task):
        if task == "":
            raise Exception("Please provide a task name.")
 