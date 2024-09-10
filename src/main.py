from os import cpu_count

import uvicorn

from config import settings


def main():
    uvicorn.run(
        'initialize:create_app',
        factory=True,
        host=settings.HOST,
        port=settings.PORT,
        workers=cpu_count()
    )


if __name__ == '__main__':
    main()
