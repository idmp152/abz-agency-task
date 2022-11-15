from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render

from workers.models import Workers


def index(request) -> HttpResponseBadRequest | HttpResponse:
    """Main workers list page"""
    workers = Workers.objects.all()
    context = {"posts": workers[:5], "count": len(workers)-5}

    return render(request, 'workers/index.html', context=context)

def show_worker(request, worker_id) -> HttpResponseBadRequest | HttpResponse:
    """Worker profile page"""
    context={"worker_id": worker_id, "worker":Workers.objects.get(pk=worker_id)}

    return render(request, 'workers/single_worker.html', context=context)
