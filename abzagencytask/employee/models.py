from django.db import models
# from django.urls import reverse

# Create your models here.

POSITIONS = (
    (1, "chief"),
    (2, "shareholder"),
    (3, "president"),
    (4, "manager"),
    (5, "employee"),
)


class Employee(models.Model):
    """There should be your comment here"""

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50, null=True, blank=True)
    position = models.CharField(max_length=50, choices=POSITIONS, default=3, null=True, blank=True)
    date_employ = models.DateTimeField(auto_now_add=True)
    salary = models.IntegerField(null=True, blank=True)
    chief = models.ForeignKey("self", null=True, blank=True, on_delete=models.PROTECT)
    image = models.ImageField(upload_to="images/employee/", null=True, blank=True)

    def __str__(self) -> str:
        return str(self.name)

    # not needed yet
    # def get_absolute_url(self) -> str:
    #     return reverse("employee", kwargs={"employee_id": self.pk})
