from functools import wraps
from fastapi import Request
from .exceptions import LoginRequiredException

def login_required(func):
    @wraps(func)
    def wrapper(request: Request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise LoginRequiredException(status_code=401)
        return func(request, *args, **kwargs)
    return wrapper