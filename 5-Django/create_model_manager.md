Model Manager Is Some Kind Of Filter On Your Model Data. For Example In Normal Situation :
`Todo.objects.all()`

Model Manager Is Something Like :
`Todo.dones.all()`

"`dones`" Is A Model Manager Here. That Filters All Done Todos. To Create This Model Manager You Need To Define a Class Like This :

```
class DoneManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=True)
```

And After That Write This In Your Model :

```
class Todo(models.Model):
    # ...
    dones = DoneManager()
    objects = models.Manager()
    # ...
```

You Define objects Here To Set Django Default Manager That Returns All Of Objects And Not Filters Them.
