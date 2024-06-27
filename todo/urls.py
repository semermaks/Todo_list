from django.urls import path, include

from .views import (
    TodoListView,
    TodoCreateView,
    TodoUpdateView,
    TodoDeleteView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    complete_task,
    uncomplete_task,
)
from django.conf import settings
from django.conf.urls.static import static

app_name = "todo"
urlpatterns = [
    path("", TodoListView.as_view(), name="task-list"),
    path(
        "task/create/",
        TodoCreateView.as_view(),
        name="task-create",
    ),
    path(
        "task/<int:pk>/update/",
        TodoUpdateView.as_view(),
        name="task-update",
    ),
    path(
        "task/<int:pk>/delete/",
        TodoDeleteView.as_view(),
        name="task-delete",
    ),
    path(
        "tag/",
        TagListView.as_view(),
        name="tag-list",
    ),
    path(
        "tag/create/",
        TagCreateView.as_view(),
        name="tag-create",
    ),
    path(
        "tag/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update",
    ),
    path(
        "tag/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete",
    ),
    path(
        "tag/<int:pk>/complete/",
        complete_task,
        name="complete-task",
    ),
    path(
        "tag/<int:pk>/uncomplete/",
        uncomplete_task,
        name="uncomplete-task",
    ),
]
