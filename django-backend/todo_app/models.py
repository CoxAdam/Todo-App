from django.db import models

class TaskList(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=255, blank=True)

    def all_tasks_completed(self):
        return all([task.is_completed for task in self.tasks.all()])

    def get_completed_tasks(self):
        return list(filter(lambda task: task.is_completed, self.tasks.all()))
        
    def __str__(self):
        return f'Task List: {self.name}'

class Task(models.Model):
    task = models.CharField(max_length=64)
    list = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name="tasks")
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f'Task: {self.task}'