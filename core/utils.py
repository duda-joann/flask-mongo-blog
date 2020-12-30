from functools import wraps
from typing import Callable

from flask import redirect, session


def login_required(function:Callable) -> Callable:
    @wraps(function)
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return function(*args, **kwargs)
        else:
            redirect('/')
    return wrapper
