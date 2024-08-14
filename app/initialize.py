from fastapi import FastAPI
from internal.routers.router import router


def create_app() -> FastAPI:
    app = FastAPI(
        root_path='/api'
    )
    app.include_router(router)

    return app
