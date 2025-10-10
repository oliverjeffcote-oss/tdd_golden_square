# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

Requirements:
* add new tasks to a todo list with status of todo
* store tasks and return a list of them to the user when requested[{},{},{}]
* The returned list should only contain items marked as "todo"
* have a flag on tasks to mark them as complete [{task: content, status: todo/complete}]

```python
# EXAMPLE

class TaskTracker:

    def __init__(self):
        # Parameters:
        #   tasks: list of dicts that contains each task
        # Side effects:
        #   Sets the list property of the self object
        self.tasks = []

    def add_task(self, task):
        # Parameters:
        #   task: string containing the task content
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task as a dict to the self object task with a status of "todo"
        pass # No code here yet

    def list_todo(self):
        # Returns:
        #   A list of only tasks that are in todo status
        # Side-effects:
        #   Throws an exception if there are no todo tasks 
        pass # No code here yet

    def mark_complete(self, task):
        # Returns:
        #  Nothing
        # Side-effects:
        #   Changes the status of the task specified from todo to complete
        pass # No code here yet

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given no tasks have been added, on initialisation
Self.tasks returns an empty list of tasks
"""
task_tracker = TaskTracker()
task_tracker.tasks = [] # should return an empty list

"""
Given a string with a task and calling #add_task 
Self.tasks returns a list with that task only and the status should be todo
"""
task_tracker = TaskTracker()
task_tracker.add_task("Walk the dog")
task_tracker.tasks => [{"task":"Walk the dog", "status": "todo"}] # Should return a list of all the tasks as dicts with their statuses

"""
Given there are 3 tasks added
#list_todo returns a list of those tasks
"""
task_tracker = TaskTracker()
task_tracker.add_task("Walk the dog")
task_tracker.add_task("Go food shopping")
task_tracker.add_task("Take car to the garage")
task_tracker.list_todo() => ["Walk the dog", "Go food shopping", "Take car to the garage"] # should return a list of the tasks that are added as new

"""
Given there is 1 task with status todo
When calling #mark_complete with the task as a string
#mark_complete changes the status attribute to "complete"
"""
task_tracker = TaskTracker()
task_tracker.add_task("Walk the dog")
task_tracker.mark_complete("Walk the dog")
task_tracker.tasks => [{"task" : "Walk the dog", "status" : "complete"}] #should show the status as complete

"""
Given there is 1 task with status todo
When calling #mark_complete with the task as a string
#list_todo returns an empty list
"""
task_tracker = TaskTracker()
task_tracker.add_task("Walk the dog")
task_tracker.mark_complete("Walk the dog")
task_tracker.list_todo() => [] #should not return complete tasks

task_tracker.list_todo() => ["Walk the dog", "Go food shopping", "Take car to the garage"] # should return a list of just the tasks that are in todo.

"""
Given there is 1 tasks with status todo and 1 complete
#list_todo returns only the one task that is in todo status
"""
task_tracker = TaskTracker()
task_tracker.add_task("Walk the dog")
task_tracker.add_task("Go food shopping")
task_tracker.add_task("Take car to the garage")
task_tracker.list_todo() => ["Walk the dog", "Go food shopping", "Take car to the garage"] # should return a list of just the tasks that are in todo.

"""
When #add_task is called with an empty string
Throws Exception asking for string to be provided
"""
task_tracker = TaskTracker()
task_tracker.add_task("") => Exception("Please provide a task") # should throw an error

"""
When #add_task is called with a type other than string
Throws Exception asking for string to be provided
"""
task_tracker = TaskTracker()
task_tracker.add_task([]) => Exception("Please provide a string") # should throw an error

"""
When #mark_complete is called with an empty string
Throws Exception asking for string to be provided
"""
task_tracker = TaskTracker()
task_tracker.mark_complete("") => Exception("Please provide a valid task") # should throw an error

"""
When #mark_complete is called with a task that isn't in the provided list
Throws Exception asking for string to be provided
"""
task_tracker = TaskTracker()
task_tracker.mark_complete("Throw a party") => Exception("Task not found in list. Please add task to mark as complete.") # should throw an error

"""
When #mark_complete is called with a task that is already complete
Returns "task already complete"
"""
task_tracker = TaskTracker()
task_tracker.add_task("Walk the dog")
task_tracker.mark_complete("Walk the dog")
task_tracker.mark_complete("Walk the dog") => "Task already marked as complete" # no side effect just returns this sentence.

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
