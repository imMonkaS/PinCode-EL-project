import uvicorn

from config.config import config


def main():
    uvicorn.run(
        'initialize:create_app',
        factory=True,
        host=config['host'],
        port=config['port'],
    )


if __name__ == '__main__':
    main()
