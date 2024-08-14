# Локальное развертывание
1. Клонировать репозиторий:
```bash
git clone 'your_repo_link'
```

2. Перейти в директорию проекта:
```bash
cd your-repo
```
3. Добавить в PYTHONPATH путь до модуля app

4. Переопределить настройки через config
```bash
cp app/config/config_tmpl.json app/config/config.json
```

5. Установить poetry, если его еще нет на вашей системе (лучше почитайте официальную документацию)

6. Установить зависимости проекта с помощью poetry:
```bash
poetry install
```
7. Установить pre-commit хуки:
```bash
poetry run pre-commit install
```
8. Запустите тесты с помощью pytest:
```bash
poetry run pytest
```

Теперь вы можете запустить сервер FastAPI:
```bash
poetry run python3 app/main.py
```
