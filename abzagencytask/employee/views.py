# pylint: disable=no-member
# pylint: disable=unused-import
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect

from employee.models import Employee
from employee.forms import BetaRegistrationForm

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

def beta_registration_form(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = BetaRegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

            try:
                _nm = form.cleaned_data["login"]
                Employee.objects.create(name=_nm, surname=_nm)
                return redirect("employee")

            # pylint: disable=bare-except
            except:
                form.add_error(None, "Login failed")

    else:
        form = BetaRegistrationForm()

    return render(request, "employee/beta_reg.html", {"form": form, "title": "Beta Registration"})
