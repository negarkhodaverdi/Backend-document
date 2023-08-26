To Make An APIView You Need To Write Something Like This :

```
class ListView(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
```

ListView Is Name Of The APIView. It Supports "`GET`" Method. Here We Get All
Todos That Are Exists And Shows It To User.

If You Want To Import These Things :

```
from rest_framework.response import Response
from api.serializers import TodoSerializer
from rest_framework.views import APIView
from todo.models import Todo
```
