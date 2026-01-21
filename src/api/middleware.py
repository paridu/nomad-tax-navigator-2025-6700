from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

# Rate Limiting setup
limiter = Limiter(key_func=get_remote_address)

class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        # Harden against XSS, Clickjacking, and MIME-sniffing
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
        response.headers["Content-Security-Policy"] = "default-src 'self'; frame-ancestors 'none';"
        return response

class InputSanitizationMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Prevent SQL Injection and NoSQL injection patterns in query params
        for key, value in request.query_params.items():
            if any(char in value for char in ["'", ";", "--", "/*", "*/"]):
                 raise HTTPException(status_code=400, detail="Invalid characters in input")
        return await call_next(request)