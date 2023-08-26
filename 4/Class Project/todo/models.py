from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    text = models.TextField(verbose_name="متن")
    status = models.BooleanField(verbose_name="انجام شده")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "لیست کار"
        verbose_name_plural = "لیست کار ها"
