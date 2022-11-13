# Generated by Django 4.1.3 on 2022-11-13 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="WorkersCtx",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=155)),
                ("surname", models.CharField(max_length=155)),
                ("patronymic", models.CharField(max_length=155)),
                ("position", models.CharField(max_length=155)),
                ("date_employ", models.DateTimeField(auto_now_add=True)),
                ("salary_amount", models.IntegerField()),
            ],
        ),
    ]