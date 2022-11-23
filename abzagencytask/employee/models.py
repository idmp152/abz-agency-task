from django.db import models

# from django.urls import reverse

# Create your models here.

# To fill in the database in `manage.py shell`
# You need to enter

# from employee.models import Employee
# from django_seed import Seed
# from random import randint

# seeder = Seed.seeder()

# seeder.add_entity(
#     Employee,
#     50,
#     {
#         "position": None,
#         "name": lambda x: seeder.faker.first_name(),
#         "surname": lambda x: seeder.faker.last_name(),
#         'chief': None,
#         'image': lambda x: f"images/employee/{randint(1, 3)}.jpg",
#     },
# )
# seeder.execute()


class Employee(models.Model):
    """There should be your comment here"""

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50, null=True, blank=True)
    position = models.ForeignKey(
        "Position",
        max_length=50,
        default=5,
        null=True,
        on_delete=models.PROTECT,
    )
    date_employ = models.DateTimeField(auto_now_add=True)
    salary = models.IntegerField(null=True, blank=True)
    chief = models.ForeignKey("self", null=True, blank=True, on_delete=models.PROTECT)
    image = models.ImageField(upload_to="images/employee/", null=True, blank=True)

    def __str__(self) -> str:
        return str(self.name)

    # not needed yet
    # def get_absolute_url(self) -> str:
    #     return reverse("employee", kwargs={"employee_id": self.pk})


class Position(models.Model):
    """There should be your comment here"""

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return str(self.name)
