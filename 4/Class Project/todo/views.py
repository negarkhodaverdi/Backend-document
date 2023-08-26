from django.shortcuts import render
from django.http import HttpResponse
from todo.models import Todo


def main(request):
    todo_list = Todo.objects.all()
    return render(request, "index.html", {"todos": todo_list})
