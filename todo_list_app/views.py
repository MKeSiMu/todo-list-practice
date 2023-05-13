from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from todo_list_app.models import Task


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "todo_list_app/index.html"
    paginate_by = 5


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_list_app:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_list_app:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo_list_app:index")


def task_complete_or_undo(request, pk):
    task = Task.objects.get(id=pk)
    if task.task_status:
        task.task_status = False
        task.save()
    else:
        task.task_status = True
        task.save()
    return redirect("/")
