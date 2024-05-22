from django.test import TestCase
from todo.models import Tag, Task


class TagModelTest(TestCase):
    def test_tag_creation(self):
        tag = Tag.objects.create(name="Test Tag")
        self.assertEqual(tag.name, "Test Tag")


class TaskModelTest(TestCase):
    def test_task_creation(self):
        tag = Tag.objects.create(name="Test Tag")
        task = Task.objects.create(
            content="Test Task Content",
            deadline_datetime=None,
            is_done=False,
        )
        task.tags.add(tag)

        self.assertEqual(task.content, "Test Task Content")
        self.assertIsNone(task.deadline_datetime)
        self.assertFalse(task.is_done)
        self.assertIn(tag, task.tags.all())
