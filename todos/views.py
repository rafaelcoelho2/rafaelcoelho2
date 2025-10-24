
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from .models import Todo

class TodoListView(ListView):
    model = Todo
    template_name = "todos/todo_list.html"  
    context_object_name = "todos"           
        
class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "description"]
    success_url = reverse_lazy("todo_list")
    
class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "description"]
    success_url = reverse_lazy("todo_list")

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")

class TodoCompletarView(View):
    """
    Classe que marca uma tarefa como concluída.
    """

    def post(self, request, pk):
        # Busca a tarefa pelo id ou retorna 404 se não existir
        todo = get_object_or_404(Todo, pk=pk)
        # Marca como concluída
        todo.is_completed = True
        # Salva a alteração no banco
        todo.save()
        # Redireciona de volta para a lista de tarefas
        return redirect("todo_list")
      