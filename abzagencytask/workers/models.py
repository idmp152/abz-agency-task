from django.db import models
from django.urls import reverse


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
    worker = models.ForeignKey('Position', null=True, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return str(self.name)

    def get_absolute_url(self) -> str:
        """Gets the service absolute url by the worker ID"""
        return reverse('worker', kwargs={'worker_id': self.pk})

class Position(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self) -> str:
        return str(self.name)

    def get_absolute_url(self) -> str:
        return reverse('position', kwargs={'position_slug': self.name})
