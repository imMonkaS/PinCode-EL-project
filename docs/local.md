# Локальное развертывание
1. Клонируйте репозиторий:
```bash
git clone 'your_repo_link'
```

2. Перейдите в директорию проекта:
```bash
cd your-repo
```
3. Добавить в PYTHONPATH путь до модуля app

4. Переопределить настройки через config
```bash
cp app/config/config_tmpl.json app/config/config.json
```

5. Установите poetry, если его еще нет на вашей системе (лучше почитайте официальную документацию)

6. Установите зависимости проекта с помощью poetry:
```bash
poetry install
```

7. Запустите тесты с помощью pytest:
```bash
poetry run pytest
```


8. Теперь вы можете запустить сервер FastAPI:
```bash
poetry run python3 app/main.py
```
