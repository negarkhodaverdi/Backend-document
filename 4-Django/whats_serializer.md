Serializers Are Made To Make Your Life Easier !

In Other Backend Frameworks You Need To Get Data From Your Database And Convert
Data To Json. For Example If You Have a variable names "`todo`" And It Contains
3 Value Named "`title`", "`text`","`status`" You Need To Make Something Like :

```
data = {
    "title":todo.title,
    "text":todo.text,
    "status":todo.status,
}
return JsonResponse(data)
```

But With Serializer :

```
serializer = TodoSerializer(todo)
return Response(serializer.data)
```

Imagine Todo Has More Than 10 Fields ! Thats Increadible !
