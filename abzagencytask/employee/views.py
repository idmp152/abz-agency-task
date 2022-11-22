# pylint: disable=no-member
# pylint: disable=unused-import
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from employee.models import Employee

# Create your views here.

DEFAULT_SHOW_COUNT = 5


def index(request: HttpRequest) -> HttpResponse:
    """Main employees list page"""

    show_count = int(request.GET.get("show_count") or DEFAULT_SHOW_COUNT)
    employees = Employee.objects.all()
    context = {
        "posts": employees[:show_count],
        "remaining": len(employees) - show_count,
    }

    return render(request, "employee/index.html", context=context)
