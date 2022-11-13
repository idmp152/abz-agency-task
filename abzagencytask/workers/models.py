from django.db import models


class WorkersCtx(models.Model):
    name = models.CharField(max_length=155)
    surname = models.CharField(max_length=155)
    patronymic = models.CharField(max_length=155)
    position = models.CharField(max_length=155)
    date_employ = models.DateTimeField(auto_now_add=True)
    salary_amount = models.IntegerField()

    def __str__(self) -> str:
        return self.name
