from django.shortcuts import render
from rest_framework.views import APIView
from todo.models import Todo
from api.serializers import TodoSerializer
from rest_framework.response import Response


class ListView(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)


class AddView(APIView):
    pass


class RemoveView(APIView):
    pass
