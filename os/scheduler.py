"""
Task scheduling.
"""

class Scheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def run(self):
        for task in self.tasks:
            task.execute()