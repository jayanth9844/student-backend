from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.api import routes_auth,routes_predict
from app.middleware.logging_middleware import LoggingMiddleware
from app.core.exceptions import regidter_exception_handlers

app = FastAPI(title="student score prediction API")

#link middleware
app.add_middleware(LoggingMiddleware)

#link endpoints
app.include_router(routes_auth.router,tags=["Auth"])
app.include_router(routes_predict.router,tags=["prediction"])

#monitoring using prometheus
Instrumentator().instrument(app).expose(app)

#add exception handler
regidter_exception_handlers(app)
