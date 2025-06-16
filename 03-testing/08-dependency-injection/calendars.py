from datetime import date, timedelta

class Calendar:
    """
    A concrete implementation of a calendar that returns the actual current date.
    This is intended for production use.
    """
    @property
    def today(self) -> date:
        """
        Returns today's actual date.
        """
        return date.today()

    def __repr__(self):
        return f"Calendar(today={self.today})"

class CalendarStub:
    """
    A stub implementation of a calendar that allows controlling the current date.
    This is highly useful for testing purposes.
    """
    def __init__(self, initial_date: date):
        """
        Initializes the CalendarStub with a specified initial date.

        Args:
            initial_date (date): The date that 'today' will initially return.
        """
        self._today = initial_date

    @property
    def today(self) -> date:
        """
        Returns the currently set 'today' date for the stub.
        """
        return self._today

    @today.setter
    def today(self, new_date: date):
        """
        Allows setting a new 'today' date for the stub.

        Args:
            new_date (date): The new date to set as 'today'.
        """
        if not isinstance(new_date, date):
            raise TypeError("today must be a datetime.date object")
        self._today = new_date

    def __repr__(self):
        return f"CalendarStub(today={self.today})"

# Example Usage for calendars.py
if __name__ == '__main__':
    print("--- Calendar Examples ---")
    real_calendar = Calendar()
    print(f"Real Calendar today: {real_calendar.today}")

    print("\n--- CalendarStub Examples ---")
    stub_calendar = CalendarStub(date(2000, 1, 1))
    print(f"Stub Calendar initial today: {stub_calendar.today}")

    stub_calendar.today = date(2001, 1, 1)
    print(f"Stub Calendar new today: {stub_calendar.today}")

    # Demonstrate setting to a future date relative to now
    future_date = date.today() + timedelta(days=30)
    stub_calendar.today = future_date
    print(f"Stub Calendar set to a future date: {stub_calendar.today}")
