from django.http import HttpResponse, HttpResponseBadRequest, HttpRequest
from django.shortcuts import redirect, render

from workers.models import Workers, Position

DEFAULT_SHOW_COUNT = 5
DEFAULT_POSITION = None
# pylint: disable=no-member


def index(request: HttpRequest) -> HttpResponseBadRequest | HttpResponse:
    """Main workers list page"""

    show_count = int(request.GET.get("show_count") or DEFAULT_SHOW_COUNT)
    position = request.GET.get("position") or DEFAULT_POSITION
    workers = (
        Workers.objects.all()
        if not position
        else Workers.objects.filter(worker__name=position)
    )
    positions = Position.objects.all()
    context = {
        "posts": workers[:show_count],
        "remaining": len(workers) - show_count,
        "positions": positions,
    }

    return render(request, "workers/index.html", context=context)


def show_worker(
    request: HttpRequest, worker_id: int
) -> HttpResponseBadRequest | HttpResponse:
    """Worker profile page"""

    context = {
        "worker_id": worker_id,
        "worker": Workers.objects.get(pk=worker_id),
    }

    return render(request, "workers/single_worker.html", context=context)

def crutch(request, position_slug) -> HttpResponse:
    return HttpResponse(
        f"there should be your advertisement here\n\n{position_slug}\n\n"
        "or did I just not figure out how to do it " + "?position request".upper())
