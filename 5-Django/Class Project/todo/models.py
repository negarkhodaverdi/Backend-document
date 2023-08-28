from django.db import models


class DoneManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=True)


class UnDoneManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=False)


class Todo(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    text = models.TextField(verbose_name="متن")
    status = models.BooleanField(verbose_name="انجام شده")
    dones = DoneManager()
    undones = UnDoneManager()
    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "لیست کار"
        verbose_name_plural = "لیست کار ها"
