To Make A Model Serializer You Need To Install Django Rest Framework First.
After That You Need To Make A File Named "`serializers.py`" In The App That You
Want To Use Serializer. For Most Cases You Need Serializers For Your "`api`" App.
We Make A "`serializers.py`" File In Our "`api`" App Here.

We Have To Import Serializer From Django Rest Framework Like This :

`from rest_framework import serializers`

After That We Can Define Our Model Serializer Like This ( Our Model Name Is
Todo Here ) :

```
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"
```

You Are Allowed To Select Fields You Want Like This Methods That Provided
Below :

- `fields = "__all__"` -> Means All Fields
- `fields = ["title","text"]` -> Means Just "title" And "text" Field.
- `exclude = ["status"]` -> Means All Fields Except "status"
