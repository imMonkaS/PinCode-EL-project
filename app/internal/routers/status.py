from fastapi import APIRouter

status_router = APIRouter()


@status_router.get('/status')
def status():
    return {
        'status': 'ok'
    }
