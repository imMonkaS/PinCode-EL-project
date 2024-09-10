from fastapi import APIRouter

STATUS_ROUTER = APIRouter()


@STATUS_ROUTER.get('/status')
def status():
    return {
        'status': 'ok'
    }
