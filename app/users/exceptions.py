from fastapi import HTTPException


class LoginRequiredException(HTTPException):
    pass

# class LoginRequiredException(Exception):
#     pass