from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic, View

from todo_list_app.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")
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


class TaskStatusUpdateView(View):
    @staticmethod
    def post(request, pk):
        task = Task.objects.get(id=pk)
        task.is_completed = not task.is_completed
        task.save()
        return redirect("todo_list_app:index")


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_name_list"
    template_name = "todo_list_app/tag_list.html"
    paginate_by = 10


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list_app:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list_app:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_list_app:tag-list")
