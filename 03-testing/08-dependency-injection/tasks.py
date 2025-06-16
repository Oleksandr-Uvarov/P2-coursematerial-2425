from datetime import date, timedelta
from calendars import Calendar # Import the Calendar class

class Task:
    """
    Represents a single task with a description, due date, and a finished status.
    """
    def __init__(self, description: str, due_date: date):
        """
        Initializes a new Task.

        Args:
            description (str): A brief description of the task.
            due_date (date): The date by which the task is due.
        """
        self._description = description
        self._due_date = due_date
        self.finished = False  # Settable field, initially False

    @property
    def description(self) -> str:
        """
        Readonly property: The description of the task.
        """
        return self._description

    @property
    def due_date(self) -> date:
        """
        Readonly property: The due date of the task.
        """
        return self._due_date

    def __repr__(self):
        """
        Returns a string representation of the Task object for easy debugging.
        """
        status = "Finished" if self.finished else "Due"
        return f"Task(description='{self.description}', due_date={self.due_date}, status='{status}')"


class TaskList:
    """
    Manages a collection of Task objects, providing methods to add,
    and categorize tasks based on their status and due dates.
    It now uses a Calendar object to determine the current date.
    """
    def __init__(self, calendar: Calendar):
        """
        Initializes an empty TaskList.

        Args:
            calendar (Calendar): An object providing the current date (e.g., Calendar or CalendarStub).
        """
        self._tasks = []
        self._calendar = calendar # Store the injected calendar dependency

    def add_task(self, task: Task):
        """
        Adds a Task to the list.

        Args:
            task (Task): The Task object to add.

        Raises:
            RuntimeError: If the task's due_date is in the past relative to the calendar's today.
        """
        if task.due_date < self._calendar.today: # Use the injected calendar's today
            raise RuntimeError("Cannot add a task with a due date in the past.")
        self._tasks.append(task)

    def __len__(self) -> int:
        """
        Returns the number of tasks in the list.
        """
        return len(self._tasks)

    @property
    def finished_tasks(self) -> list[Task]:
        """
        Returns a list of all tasks that are marked as finished.
        """
        return [task for task in self._tasks if task.finished]

    @property
    def due_tasks(self) -> list[Task]:
        """
        Returns a list of all unfinished tasks.
        """
        return [task for task in self._tasks if not task.finished]

    @property
    def overdue_tasks(self) -> list[Task]:
        """
        Returns a list of all unfinished tasks whose due_date is in the past
        relative to the calendar's today.
        """
        current_date = self._calendar.today # Use the injected calendar's today
        return [task for task in self._tasks if not task.finished and task.due_date < current_date]

    def __repr__(self):
        """
        Returns a string representation of the TaskList object.
        """
        if not self._tasks:
            return "TaskList: (empty)"
        task_strings = "\n  ".join(repr(task) for task in self._tasks)
        return f"TaskList:\n  {task_strings}"


# Example Usage (as provided in the problem description, for testing purposes)
if __name__ == '__main__':
    # When running the main script, we use the real Calendar
    from calendars import Calendar, CalendarStub

    print("--- Task Class Examples ---")
    task = Task('bake birthday cake', date(2023, 10, 1))
    print(f"Description: {task.description}")
    print(f"Due Date: {task.due_date}")
    print(f"Finished: {task.finished}")
    task.finished = True
    print(f"Finished after setting: {task.finished}")
    print(f"Task representation: {task}")

    print("\n--- TaskList Class Examples (with real Calendar) ---")
    real_calendar = Calendar()
    tasks = TaskList(real_calendar) # Pass the real calendar
    print(f"Initial TaskList length: {len(tasks)}")

    tomorrow = real_calendar.today + timedelta(days=1)
    yesterday = real_calendar.today - timedelta(days=1)

    # Adding task with due_date in past is forbidden
    print("\nAttempting to add a task with a past due date (should raise RuntimeError):")
    try:
        task_in_past = Task('some description', yesterday)
        tasks.add_task(task_in_past)
    except RuntimeError as e:
        print(f"Caught expected error: {e}")

    # Adding task with due_date in future works
    print("\nAdding a task with a future due date:")
    task_future = Task('buy groceries', tomorrow)
    tasks.add_task(task_future)
    print(f"TaskList length after adding: {len(tasks)}")
    print(f"Finished tasks: {tasks.finished_tasks}")
    print(f"Due tasks: {tasks.due_tasks}")
    print(f"Overdue tasks: {tasks.overdue_tasks}")
    print(f"TaskList representation: {tasks}")

    # Add a task that is due today
    print("\nAdding a task due today:")
    task_just_due = Task('pay bills', real_calendar.today)
    tasks.add_task(task_just_due)
    print(f"Due tasks (including today's): {tasks.due_tasks}")
    print(f"Overdue tasks (should be empty if due today): {tasks.overdue_tasks}")


    # Mark a task as finished
    print("\nMarking 'buy groceries' task as finished:")
    task_future.finished = True
    print(f"Finished tasks: {tasks.finished_tasks}")
    print(f"Due tasks: {tasks.due_tasks}")
    print(f"Overdue tasks: {tasks.overdue_tasks}")
    print(f"TaskList representation: {tasks}")

    print("\n--- TaskList Class Examples (with CalendarStub for specific date) ---")
    stub_calendar = CalendarStub(date(2023, 1, 15)) # Set a specific date for testing
    stub_tasks = TaskList(stub_calendar)

    task1 = Task('Do laundry', date(2023, 1, 10)) # Overdue for stub_calendar
    task2 = Task('Call mom', date(2023, 1, 20))  # Future for stub_calendar
    task3 = Task('Read book', date(2023, 1, 14)) # Overdue for stub_calendar

    stub_tasks.add_task(task2) # Add future task successfully

    # Try adding an overdue task from the stub's perspective
    try:
        stub_tasks.add_task(task1)
    except RuntimeError as e:
        print(f"Caught expected error (from stub): {e}")

    stub_calendar.today = date(2023, 1, 5) # Change stub date to allow task1 and task3
    stub_tasks.add_task(task1)
    stub_tasks.add_task(task3)

    print(f"\nStub Calendar today: {stub_calendar.today}")
    print(f"Stub TaskList due tasks: {stub_tasks.due_tasks}")
    print(f"Stub TaskList overdue tasks (expected empty here): {stub_tasks.overdue_tasks}")

    stub_calendar.today = date(2023, 1, 25) # Advance stub date to make tasks overdue

    print(f"\nStub Calendar today (advanced): {stub_calendar.today}")
    print(f"Stub TaskList due tasks: {stub_tasks.due_tasks}")
    print(f"Stub TaskList overdue tasks (expected task1 and task3): {stub_tasks.overdue_tasks}")
    task1.finished = True
    print(f"Stub TaskList overdue tasks (after finishing task1): {stub_tasks.overdue_tasks}")

