from django.http import (
    HttpRequest, HttpResponse, HttpResponseBadRequest
)
from django.shortcuts import render

from workers.models import WorkersCtx


def index(request: HttpRequest, hierarchy_id: int) -> HttpResponse:
    """Index view for the workers app."""
    if request.GET is None:
        return HttpResponseBadRequest()

    return HttpResponse(f"<h1>Hierarchy by ID {hierarchy_id}:</h1>\n" +
                                '\n'.join(f"<p>{i}. Вячеслав Бебрович</p>"
                                    for i in map(str, range(hierarchy_id)))) # type: ignore

# POST DB
def test(request) -> HttpResponse:
    posts = WorkersCtx.objects.all()
    return render(request, "workers/index.html", {"posts": posts})
