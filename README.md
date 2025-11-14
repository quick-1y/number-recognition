# Number Recognition Platform

Полноценный скелет системы автоматического распознавания и обработки автомобильных номерных знаков. Проект включает backend (FastAPI), frontend (React + Vite), инфраструктурные компоненты (PostgreSQL, MinIO, Prometheus, Grafana) и документацию.

## Структура репозитория

```
backend/              # FastAPI-приложение и тесты
frontend/             # Web-интерфейс администратора и оператора
ops/                  # Конфигурации мониторинга (Prometheus)
docs/                 # Архитектурная документация
Dockerfile / compose  # Запуск всей системы через Docker Compose
```

## Быстрый старт через Docker Compose

```bash
docker compose up --build
```

Доступы по умолчанию:
- Backend API: http://localhost:8000/api
- Frontend: http://localhost:5173
- PostgreSQL: localhost:5432 (user/password/db: `anpr`)
- MinIO: http://localhost:9000 (консоль http://localhost:9001, доступ `anpr` / `anpr_secret`)
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000

## Запуск backend локально

```bash
cd backend
poetry install
poetry run uvicorn app.main:app --reload
```

Эндпоинты здоровья: `/api/diagnostics/health`, `/api/diagnostics/ready`, `/api/diagnostics/live`. Метрики Prometheus по пути `/metrics`.

## Запуск frontend локально

```bash
cd frontend
npm install
npm run dev
```

URL API настраивается переменной `VITE_API_URL` (по умолчанию `http://localhost:8000/api`).

## Тестирование

```bash
cd backend
poetry run pytest
```

## PyCharm

В каталоге `.run` размещена конфигурация `Backend (Uvicorn).run.xml`, позволяющая запустить backend в PyCharm (Run → Run…).

1. Откройте проект в PyCharm и дождитесь индексирования.
2. Убедитесь, что виртуальное окружение (Poetry или другое) активировано и в нём установлены зависимости из `backend/pyproject.toml`.
3. В меню **Run → Edit Configurations…** выберите `Backend (Uvicorn)`.
4. Проверьте, что в секции **Execution** отмечен пункт **Execute using a module** и в поле **Module name** указано `uvicorn` (PyCharm подставляет команду `python -m uvicorn`).
5. Рабочая директория должна указывать на `$PROJECT_DIR$/backend`, чтобы путь `app.main:app` разрешался корректно.
6. Нажмите **Run** — сервер будет запущен в режиме Hot Reload (`--reload`).

Если конфигурация не появилась автоматически, добавьте новый Python Run Configuration с типом «Module name», значением `uvicorn` и параметрами `app.main:app --reload` вручную.

## Архитектура

Подробная декомпозиция модулей, компонент и требований приведена в [docs/architecture.md](docs/architecture.md).

## Переменные окружения

Скопируйте `backend/.env.example` в `backend/.env` и при необходимости обновите значения.

## Дальнейшие шаги

- Подключение реальных реализаций детектора, трекера и OCR.
- Интеграция с настоящей БД через SQLAlchemy/Alеmbic.
- Реализация очередей вебхуков, аудита и RBAC на уровне БД.
