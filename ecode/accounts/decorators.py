from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

def role_required(**allowed_roles):
    def decorator(view_func):
        @login_required
        def wrapped(request, *args, **kwargs):
            if request.user.profile.role not in allowed_roles:
                return HttpResponseForbidden("Доступ запрещен")
            return view_func(request, *args, **kwargs)
        return wrapped
    return decorator