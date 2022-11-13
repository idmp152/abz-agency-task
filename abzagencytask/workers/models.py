from django.db import models


class Workers(models.Model):
    """Workers main app model."""
    name = models.CharField(max_length=155)
    surname = models.CharField(max_length=155)
    patronymic = models.CharField(max_length=155)
    position = models.CharField(max_length=155)
    date_employ = models.DateTimeField(auto_now_add=True)
    chief = models.ForeignKey(to='self', null=True, blank=True, on_delete=models.CASCADE)
    salary_amount = models.IntegerField(null=True, blank=True)
    photo = models.ImageField(upload_to="images/workers/")

    def __str__(self) -> str:
        return str(self.name)
