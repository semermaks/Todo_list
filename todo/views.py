from django.db.models import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from todo.forms import TodoForm, TagSearchForm, TodoSearchForm
from todo.models import Task, Tag


class TodoListView(generic.ListView):
    model = Task
    template_name = 'todo/task_list.html'
    context_object_name = 'tasks'
    ordering = ['is_done', '-created_datetime']

    def get_context_data(self, **kwargs) -> dict:
        context = super(TodoListView, self).get_context_data(**kwargs)
        content = self.request.GET.get("content", "")
        context["search_form"] = TodoSearchForm(
            {"content": content}
        )
        return context

    def get_queryset(self) -> QuerySet:
        queryset = Task.objects.all()
        form = TodoSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                content__icontains=form.cleaned_data["content"]
            )
        return super().get_queryset()


class TodoCreateView(generic.CreateView):
    model = Task
    form_class = TodoForm
    success_url = reverse_lazy("todo:task-list")


class TodoUpdateView(generic.UpdateView):
    model = Task
    form_class = TodoForm
    success_url = reverse_lazy("todo:task-list")


class TodoDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task-list")
    template_name = "todo/task_confirm_delete.html"


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "todo/tag_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = TagSearchForm(
            initial={
                "name": name,
            }
        )
        return context

    def get_queryset(self) -> QuerySet:
        queryset = Tag.objects.all()
        form = TagSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return super().get_queryset()


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")


def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = True
    task.save()
    return redirect("todo:task-list")


def uncomplete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = False
    task.save()
    return redirect("todo:task-list")
