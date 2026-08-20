# Decorator for formatting report
def report_decorator(function):
    def wrapper(self):
        print("=" * 40)
        function(self)
        print("=" * 40)
    return wrapper


class Report:

    # Class variable
    report_count = 0

    # Constructor (Magic Method)
    def __init__(self, title, content):
        self.title = title
        self.content = content
        Report.report_count += 1

    # Magic Method
    def __str__(self):
        return f"Report Title: {self.title}"

    # Class Method
    @classmethod
    def total_reports(cls):
        print("Total Reports Created:", cls.report_count)

    # Decorator applied
    @report_decorator
    def generate(self):
        print("REPORT")
        print("Title :", self.title)
        print("Content :", self.content)


# ---------------- Main Program ----------------

# User input
title = input("Enter Report Title: ")
content = input("Enter Report Content: ")

# Create object
r1 = Report(title, content)

# Display report
r1.generate()

# Using magic method
print(r1)

# Display total reports
Report.total_reports()