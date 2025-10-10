from lib.task_tracker import TaskTracker

def test_empty_task_list_returned():
    task_tracker = TaskTracker()
    assert task_tracker.tasks == []

def test_add_task_adds_to_tasks_list():
    task_tracker = TaskTracker()
    task_tracker.add_task("Walk the dog")
    assert task_tracker.tasks == [{"task":"Walk the dog", "status": "to do"}]

def test_add_more_than_one_task_adds_to_tasks_list():
    task_tracker = TaskTracker()
    task_tracker.add_task("Walk the dog")
    task_tracker.add_task("Go to the shops")
    task_tracker.add_task("Make lunch")
    assert task_tracker.tasks == [{"task":"Walk the dog", "status": "to do"}, {"task":"Go to the shops", "status": "to do"},{"task":"Make lunch", "status": "to do"}]

def test_returns_list_of_tasks():
    task_tracker = TaskTracker()
    task_tracker.add_task("Walk the dog")
    task_tracker.add_task("Go to the shops")
    task_tracker.add_task("Make lunch")
    assert task_tracker.list_todo() == ["Walk the dog", "Go to the shops", "Make lunch"]