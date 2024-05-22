from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    deadline_datetime = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="task")

    class Meta:
        ordering = ['is_done', '-created_datetime']

    def __str__(self):
        return f"Task: {self.content} ({self.created_datetime.strftime('%Y-%m-%d %H:%M')})"
