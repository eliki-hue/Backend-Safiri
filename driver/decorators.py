from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return view_function(request, *args, **kwargs)
        return view_function(*args, **kwargs)
    return wrapper_function

def allowed_users(allowed_roles=[]):
    def decorator(view_function):
        def wrapper_function(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
                print(group)
            if group in allowed_roles:
                return view_function(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page.')
        return wrapper_function
    return decorator