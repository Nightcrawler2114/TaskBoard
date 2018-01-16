from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Task


@method_decorator(login_required, name='dispatch')
class TaskListView(ListView):
    model = Task

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


@method_decorator(login_required, name='dispatch')
class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description']
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('task:task_list')


@method_decorator(login_required, name='dispatch')
class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'description']
    success_url = '/'
    template_name_suffix = '_update_form'



