from django.http import HttpResponse, HttpResponseBadRequest, HttpRequest
from django.shortcuts import render

from workers.models import Workers

DEFAULT_SHOW_COUNT = 5

def index(request: HttpRequest) -> HttpResponseBadRequest | HttpResponse:
    """Main workers list page"""
    show_count = int(request.GET.get("show_count") or DEFAULT_SHOW_COUNT)
    workers = Workers.objects.all() # pylint: disable=no-member
    context = {"posts": workers[:show_count], "remaining": len(workers) - show_count}

    return render(request, 'workers/index.html', context=context)

def show_worker(request: HttpRequest, worker_id: int) -> HttpResponseBadRequest | HttpResponse:
    """Worker profile page"""
    context={"worker_id": worker_id, "worker":Workers.objects.get(pk=worker_id)} # pylint: disable=no-member

    return render(request, 'workers/single_worker.html', context=context)
