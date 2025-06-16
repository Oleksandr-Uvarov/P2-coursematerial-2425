import unittest
from datetime import date, timedelta
from tasks import Task, TaskList
from calendars import CalendarStub

class TestTaskListOverdue(unittest.TestCase):
    """
    Test suite for the TaskList class, specifically focusing on overdue task functionality
    using a CalendarStub for controlled date testing.
    """

    def test_task_becomes_overdue(self):
        """
        Tests that a task correctly becomes overdue when the simulated date
        advances past its due date.
        """
        # 1. Arrange: Set up initial state with CalendarStub
        initial_test_date = date(2023, 1, 1) # Our starting "today" for the test
        calendar_stub = CalendarStub(initial_test_date)
        task_list = TaskList(calendar_stub) # Inject the stub calendar

        # Create a task due "tomorrow" relative to our initial_test_date
        # So, due_date will be 2023-01-02
        tomorrow_from_initial = initial_test_date + timedelta(days=1)
        task = Task('some description', tomorrow_from_initial)
        task_list.add_task(task)

        # At this point, the task should not be overdue
        self.assertNotIn(task, task_list.overdue_tasks)
        self.assertIn(task, task_list.due_tasks)
        self.assertEqual(len(task_list.overdue_tasks), 0)
        self.assertEqual(len(task_list.due_tasks), 1)

        # 2. Act: Simulate waiting 2 days by advancing the CalendarStub's date
        # New "today" will be 2023-01-03
        calendar_stub.today = initial_test_date + timedelta(days=2)

        # 3. Assert: Check if the task is now overdue
        self.assertIn(task, task_list.overdue_tasks)
        self.assertNotIn(task, task_list.due_tasks) # It's no longer just "due", it's "overdue"
        self.assertEqual(len(task_list.overdue_tasks), 1)
        self.assertEqual(task_list.overdue_tasks[0], task)
        self.assertEqual(len(task_list.due_tasks), 0) # No tasks left that are "due" but not "overdue"

    def test_finished_task_is_never_overdue(self):
        """
        Tests that a finished task is never considered overdue, regardless of date.
        """
        initial_test_date = date(2023, 1, 1)
        calendar_stub = CalendarStub(initial_test_date)
        task_list = TaskList(calendar_stub)

        # Create a task that will become overdue
        due_date_past = initial_test_date - timedelta(days=5) # Due date in the past relative to initial_test_date
        task = Task('finished overdue task', due_date_past)

        # Initially, try to add it (should fail due to past date)
        # We need to set the stub date to allow adding this task
        calendar_stub.today = due_date_past - timedelta(days=1) # Set stub to day before due date
        task_list.add_task(task)

        task.finished = True # Mark it as finished

        # Advance the date significantly
        calendar_stub.today = initial_test_date + timedelta(days=10)

        # The finished task should not appear in overdue_tasks
        self.assertNotIn(task, task_list.overdue_tasks)
        self.assertIn(task, task_list.finished_tasks)
        self.assertEqual(len(task_list.overdue_tasks), 0)

    def test_multiple_overdue_tasks(self):
        """
        Tests that multiple tasks correctly appear in the overdue list.
        """
        initial_test_date = date(2023, 3, 1)
        calendar_stub = CalendarStub(initial_test_date)
        task_list = TaskList(calendar_stub)

        # Tasks due in the future
        task1 = Task('Task A', initial_test_date + timedelta(days=1))
        task2 = Task('Task B', initial_test_date + timedelta(days=3))
        task_list.add_task(task1)
        task_list.add_task(task2)

        self.assertEqual(len(task_list.overdue_tasks), 0)

        # Advance date to make task1 overdue, task2 still due
        calendar_stub.today = initial_test_date + timedelta(days=2)
        self.assertIn(task1, task_list.overdue_tasks)
        self.assertNotIn(task2, task_list.overdue_tasks)
        self.assertEqual(len(task_list.overdue_tasks), 1)

        # Advance date to make both task1 and task2 overdue
        calendar_stub.today = initial_test_date + timedelta(days=5)
        self.assertIn(task1, task_list.overdue_tasks)
        self.assertIn(task2, task_list.overdue_tasks)
        self.assertEqual(len(task_list.overdue_tasks), 2)

    def test_add_task_with_past_due_date_using_stub(self):
        """
        Tests that adding a task with a due date in the past relative to the
        stub's current date raises a RuntimeError.
        """
        initial_test_date = date(2024, 5, 15)
        calendar_stub = CalendarStub(initial_test_date)
        task_list = TaskList(calendar_stub)

        past_due_date = initial_test_date - timedelta(days=1)
        task_in_past = Task('Task with past date', past_due_date)

        with self.assertRaises(RuntimeError) as cm:
            task_list.add_task(task_in_past)
        self.assertIn("Cannot add a task with a due date in the past.", str(cm.exception))


# To run these tests, save them as tests.py and run:
# python -m unittest tests.py
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

