from fastapi import FastAPI

from routers.router import router


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router)

    return app
