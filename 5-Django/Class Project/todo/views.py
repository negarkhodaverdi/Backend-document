from django.shortcuts import render
from todo.models import Todo


def main(request):
    todo_list = Todo.objects.filter(title__contains="تست")
    return render(request, "index.html", {"todos": todo_list})
