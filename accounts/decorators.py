from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    """Allows to see page only for unauthenticated users. Otherwise redirect to home page"""
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_users(allowed_roles=[]):
    """Allows to see page only for users from specific group(s)"""
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('user')
        return wrapper_func
    return decorator


"""
def admin_only(view_func):
'''Allows to see home page for admin user only, for other redirect to users page.'''
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'customer':
            return redirect('user')
        if group == 'admin':
            return view_func(request, *args, **kwargs)
    return wrapper_function
"""