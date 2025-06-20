from datetime import date, timedelta

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
    """
    def __init__(self):
        """
        Initializes an empty TaskList.
        """
        self._tasks = []

    def add_task(self, task: Task):
        """
        Adds a Task to the list.

        Args:
            task (Task): The Task object to add.

        Raises:
            RuntimeError: If the task's due_date is in the past.
        """
        if task.due_date < date.today():
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
        Returns a list of all unfinished tasks whose due_date is in the past.
        """
        today = date.today()
        return [task for task in self._tasks if not task.finished and task.due_date < today]

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
    print("--- Task Class Examples ---")
    task = Task('bake birthday cake', date(2023, 10, 1))
    print(f"Description: {task.description}")
    print(f"Due Date: {task.due_date}")
    print(f"Finished: {task.finished}")
    task.finished = True
    print(f"Finished after setting: {task.finished}")
    print(f"Task representation: {task}")

    print("\n--- TaskList Class Examples ---")
    tasks = TaskList()
    print(f"Initial TaskList length: {len(tasks)}")

    tomorrow = date.today() + timedelta(days=1)
    yesterday = date.today() - timedelta(days=1)

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

    # Simulate waiting two days (for demonstration, won't actually wait)
    # To properly test overdue, you'd run this script on different days or mock date.today()
    print("\nSimulating tasks becoming overdue (manual check needed, as date.today() is static for this run):")
    task_just_due = Task('pay bills', date.today()) # Task due today, will not be overdue yet
    tasks.add_task(task_just_due)
    print(f"Due tasks (including today's): {tasks.due_tasks}")
    print(f"Overdue tasks (still empty for this run unless due_date was yesterday): {tasks.overdue_tasks}")

    # Mark a task as finished
    print("\nMarking 'buy groceries' task as finished:")
    task_future.finished = True
    print(f"Finished tasks: {tasks.finished_tasks}")
    print(f"Due tasks: {tasks.due_tasks}")
    print(f"Overdue tasks: {tasks.overdue_tasks}")
    print(f"TaskList representation: {tasks}")

    # Add a task that will definitely be overdue if this script runs tomorrow
    task_tomorrow_overdue = Task('review report', date.today() + timedelta(days=1))
    tasks.add_task(task_tomorrow_overdue)
    print(f"\nAdded task due tomorrow: {task_tomorrow_overdue}")
    print(f"Due tasks: {tasks.due_tasks}")
    print(f"Overdue tasks: {tasks.overdue_tasks}")

