from fastapi import FastAPI

from configs.settings import settings

app = FastAPI(
        debug=settings.debug,
        docs_url="/api/docs",
        title="Search Model API",
        version="0.1.0"
    )