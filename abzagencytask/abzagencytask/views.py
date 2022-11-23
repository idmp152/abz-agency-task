from django.http import Http404, HttpResponseNotFound, HttpRequest, HttpResponse
from django.shortcuts import redirect

def root_index(_: HttpRequest) -> HttpResponse: # Request is ignored
    """Root index page."""
    return redirect('employee/')

def not_found_handler(request: HttpRequest, _: Http404) -> HttpResponseNotFound:
    """404 Not Found error handler for the Workers app"""
    return HttpResponseNotFound(f"Resource not found: {request.path}")
