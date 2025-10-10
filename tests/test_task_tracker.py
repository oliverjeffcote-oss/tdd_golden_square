from lib.task_tracker import TaskTracker
import pytest

"""
Given no tasks have been added, on initialisation
Self.tasks returns an empty list of tasks
"""
def test_empty_task_list_returned():
    task_tracker = TaskTracker()
    assert task_tracker.tasks == []

"""
Given a string with a task and calling #add_task 
Self.tasks returns a list with that task only and the status should be todo
"""
def test_add_task_adds_to_tasks_list():
    task_tracker = TaskTracker()
    task_tracker.add_task("Walk the dog")
    assert task_tracker.tasks == [{"task":"Walk the dog", "status": "to do"}]

"""
Given there are 3 tasks added
Task_tracker contains the 3 dictionaries of each task.
"""
def test_add_more_than_one_task_adds_to_tasks_list():
    task_tracker = TaskTracker()
    task_tracker.add_task("Walk the dog")
    task_tracker.add_task("Go to the shops")
    task_tracker.add_task("Make lunch")
    assert task_tracker.tasks == [{"task":"Walk the dog", "status": "to do"}, {"task":"Go to the shops", "status": "to do"},{"task":"Make lunch", "status": "to do"}]

"""
Given three tasks are added
#list_todo returns a list of those tasks as strings
"""
def test_returns_list_of_tasks():
    task_tracker = TaskTracker()
    task_tracker.add_task("Walk the dog")
    task_tracker.add_task("Go to the shops")
    task_tracker.add_task("Make lunch")
    assert task_tracker.list_todo() == ["Walk the dog", "Go to the shops", "Make lunch"]

"""
Given there is 1 task with status todo
When calling #mark_complete with the task as a string
#mark_complete changes the status attribute to "complete"
"""
def test_mark_complete_changes_status_to_complete():
    task_tracker = TaskTracker()
    task_tracker.add_task("Go to the shops")
    task_tracker.mark_complete("Go to the shops")
    assert task_tracker.tasks == [{"task" : "Go to the shops", "status" : "complete"}]

"""
Given there is 1 task with status todo
When calling #mark_complete with the task as a string
#list_todo returns an empty list
"""
def test_return_empty_list_where_all_tasks_are_completed():
    task_tracker = TaskTracker()
    task_tracker.add_task("Make lunch")
    task_tracker.mark_complete("Make lunch")
    assert task_tracker.list_todo() == []

"""
Given there is 1 task with status todo and 1 complete
#list_todo returns only the one task that is in todo status
"""
def test_only_one_todo_task_returned():
    task_tracker = TaskTracker()
    task_tracker.add_task("Go food shopping")
    task_tracker.add_task("Take car to the garage")
    task_tracker.mark_complete("Take car to the garage")
    assert task_tracker.list_todo() == ["Go food shopping"] 
# should return a list of just the tasks that are in todo.

"""
When #add_task is called with an empty string
Throws Exception asking for string to be provided
"""
def test_empty_string_provided_for_task_throws_error():
    task_tracker = TaskTracker()
    with pytest.raises(Exception) as e:
        task_tracker.add_task("")
    assert str(e.value) == "Please provide a task name."

"""
When #mark_complete is called with an empty string
Throws Exception asking for string to be provided
"""
def test_empty_string_provided_for_mark_complete_throws_error():
    task_tracker = TaskTracker()
    with pytest.raises(Exception) as e:
        task_tracker.mark_complete("")
    assert str(e.value) == "Please provide a task name."

"""
When #mark_complete is called with a task that isn't in the provided list
Throws Exception asking for string to be provided
"""
def test_mark_complete_throws_error_when_nonexistent_task_name_requested():
    task_tracker = TaskTracker()
    with pytest.raises(Exception) as e:
        task_tracker.mark_complete("Walk the dog")
    assert str(e.value) == "Task not found."

"""
When #mark_complete is called with a task that is already complete
Returns "task already complete"
"""

def test_alert_user_that_task_is_already_completed():
    task_tracker = TaskTracker()
    task_tracker.add_task("Walk the dog")
    task_tracker.mark_complete("Walk the dog")
    assert task_tracker.mark_complete("Walk the dog") == "Task is already completed."