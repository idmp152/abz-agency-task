from django.contrib import admin

# Register your models here.

from employee.models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "surname",
        "position",
        "chief",
        "salary",
        "date_employ",
    )
    list_display_links = ("id", "name", "surname")
    list_filter = ("date_employ",)
    search_fields = ("id", "name")


admin.site.register(Employee, EmployeeAdmin)
