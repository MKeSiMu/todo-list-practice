from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Task(models.Model):
    TASK_STATUS_CHOICES = [(False, 'Not done'), (True, 'Done')]
    content = models.CharField(max_length=250)
    created_datetime = models.DateTimeField(auto_now_add=True)
    deadline_datetime = models.DateTimeField(
        default=timezone.now,
        null=True,
        blank=True,
        help_text="Enter date and time in '2023-05-13 06:31' format"
    )
    task_status = models.BooleanField(default=False, choices=TASK_STATUS_CHOICES)
    tag = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["task_status", "-created_datetime"]

    def __str__(self):
        return self.content
