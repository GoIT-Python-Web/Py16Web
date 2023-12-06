from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


class CustomHeaderMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super(CustomHeaderMiddleware, self).__init__(app)

    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        response.headers['Custom'] = 'Example'
        return response

