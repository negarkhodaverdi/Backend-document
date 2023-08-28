from django.shortcuts import render
from rest_framework.views import APIView
from todo.models import Todo
from api.serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class ListView(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)


class AddView(APIView):
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.data)
            return Response({"message": "Done"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class RemoveView(APIView):
    def get(self, request):
        todo_id = request.GET["id"]
        todo_object = get_object_or_404(Todo, id=todo_id)
        todo_object.delete()
        return Response({"message": "Done"}, status=status.HTTP_200_OK)
