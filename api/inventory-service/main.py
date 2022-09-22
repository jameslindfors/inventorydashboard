"""Main Entrypoint"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from v1.api import register_v1

from core.config import settings


def get_application():
    """ Initialize App

    Returns:
        app: return app instance
    """
    _app = FastAPI(title=settings.app_name,
            version=settings.app_version,
            openapi_url=f"/{settings.uri_prefix}/openapi.json",
            docs_url=f"/{settings.uri_prefix}/docs")

    _app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
    )

    return _app

app = get_application()
register_v1(app)
