from fastapi import FastAPI

from configs.settings import settings

def create_app():
    app = FastAPI(
        debug=settings.debug,
        docs_url="/api/docs",
        title="Search Model API",
        version="0.1.0"
    )

    return app