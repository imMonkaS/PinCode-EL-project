import sys

import uvicorn

from config.config import config
from internal.db.db import Database


def main():
    if len(sys.argv) > 1 and 'test_data' in sys.argv:
        Database.fill_database_with_test_data()

    uvicorn.run(
        'initialize:create_app',
        factory=True,
        host=config['host'],
        port=config['port'],
        workers=1
    )


if __name__ == '__main__':
    main()
