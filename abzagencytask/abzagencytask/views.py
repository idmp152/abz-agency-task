from django.http import Http404, HttpResponseNotFound, HttpRequest

def not_found_handler(request: HttpRequest, _: Http404) -> HttpResponseNotFound:
    """404 Not Found error handler for the Workers app"""
    return HttpResponseNotFound(f"Resource not found: {request.path}")
