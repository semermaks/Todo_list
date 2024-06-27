from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from todo.models import Task


class TodoForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("content", "deadline_datetime", "tags")
        widgets = {
            "deadline_datetime": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }


class TodoSearchForm(forms.Form):
    content = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by content"}),
    )


class TagSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"}),
    )
