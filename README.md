# Backend без магии 🧱

Привет! Это практикум для двух backend-разработчиков команды «ЧтоДальше». **Синтаксис Python здесь не объясняем.** Вместо этого учимся собирать сервер из понятных частей: HTTP → FastAPI → Pydantic → PostgreSQL → SQLAlchemy → Alembic → тесты.

Репозиторий — **не готовое решение**: сейчас здесь есть только маленький рабочий сервер с `GET /health`. Остальное вы допишете по заданиям. Ошибаться можно — это учебная площадка!

## Сначала установите

- [Python 3.12+](https://www.python.org/downloads/) и [VS Code](https://code.visualstudio.com/).
- [Git](https://git-scm.com/downloads). Если ещё не работали с Git, пройдите [наш практикум](https://github.com/tishelka/git-training).
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) — **понадобится с урока про PostgreSQL**, не на старте.

## Шаг 1. Скачайте проект

```bash
git clone https://github.com/tishelka/backend-training.git
cd backend-training
```

### Windows (PowerShell)

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
```

Если `py -3.12` нет, но подходящий Python установлен, попробуйте `python -m venv .venv`. Если PowerShell не разрешает активацию, **не нужно ослаблять системную политику**: запускайте Python напрямую:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
```

В VS Code выберите интерпретатор из `.venv`: Ctrl/Cmd+Shift+P → **Python: Select Interpreter**.

## Шаг 2. Запустите FastAPI

```bash
python -m uvicorn app.main:app --reload
```

Откройте:
- [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health) — увидите `{"status":"ok"}`.
- **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) — Swagger UI!** Нажмите на GET /health → **Try it out** → **Execute** и посмотрите ответ.
- [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) — другой вид документации.
- [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json) — машинное описание API.

Остановить сервер можно Ctrl+C. `--reload` перезапускает его после правок в файлах.

### А если создавать FastAPI-проект с нуля?

В пустой папке достаточно создать `.venv`, установить `fastapi` и `uvicorn`, создать `app/__init__.py` и `app/main.py`:

```python
from fastapi import FastAPI

app = FastAPI(title="Мой первый сервер")

@app.get("/health")
def health():
    return {"status": "ok"}
```

Запустите `python -m uvicorn app.main:app --reload`. Это весь минимальный сервер. Остальные файлы появятся тогда, когда реально понадобятся.

## Как устроен практикум

| № | Урок | Главное |
| - | - | - |
| 01 | [HTTP и REST](docs/01-http-and-rest.md) | Кто отправляет запросы и что значит 404 |
| 02 | [Первый FastAPI](docs/02-fastapi.md) | GET, POST, параметры маршрутов |
| 03 | [Swagger / OpenAPI](docs/03-swagger.md) | Тестируем API через браузер |
| 04 | [Pydantic v2](docs/04-pydantic.md) | Правильные данные и ошибки 422 |
| 05 | [APIRouter и Depends](docs/05-routers-and-dependencies.md) | Разносим код по модулям |
| 06 | [PostgreSQL и SQL](docs/06-postgresql.md) | Таблицы, ключи и запросы |
| 07 | [SQLAlchemy + psycopg](docs/07-sqlalchemy.md) | Работа с базой из Python |
| 08 | [Alembic](docs/08-alembic.md) | Обновляем схему, не теряя данные |
| 09 | [Pytest, HTTPX, Ruff](docs/09-testing.md) | Тестируем сервер |
| 10 | [Docker, настройки, ошибки](docs/10-docker-and-config.md) | Запуск проекта на разных ПК |
| 11 | [Seed, upsert и реальный MVP](docs/11-seed-and-architecture.md) | Как устроено «ЧтоДальше» |
| — | [Если что-то сломалось](docs/12-troubleshooting.md) | Частые ошибки |

**Практика:** [01](exercises/01-first-api.md) → [02](exercises/02-swagger-and-params.md) → [03](exercises/03-validation.md) → [04](exercises/04-routers.md) → [05](exercises/05-postgres.md) → [06](exercises/06-crud.md) → [07](exercises/07-migrations.md) → [08](exercises/08-tests.md) → [09 (финал)](exercises/09-final-project.md).

Сначала читайте короткий урок, затем самостоятельно выполняйте задание. **Не переписывайте целиком готовый backend MVP.** После каждого шага объясните напарнику, почему решение работает.

## Когда дойдёте до PostgreSQL

Запустите Docker Desktop и выполните:

```bash
docker compose up -d db
docker compose ps
```

PostgreSQL поднимется на `localhost:5432`; данные переживут перезапуск контейнера. API можно продолжать запускать локально. Позже `docker compose up --build` поднимет обе службы; не запускайте два сервера сразу на порту 8000.

Учебные логин и пароль PostgreSQL — `training` / `training`, только для **локального** стенда. Не публикуйте такую БД в интернете.

## Проверка стартового проекта

```bash
python -m pytest -q
python -m ruff check .
```

## Как сдавать задания

Читайте [CONTRIBUTING.md](CONTRIBUTING.md). Лучше каждому создать **fork**: задания меняют одни и те же файлы, поэтому работать всем сразу в одной папке `app/` неудобно. Дальше создавайте ветку на упражнение, коммит, push и PR **в свой fork** — руководителю отправляйте ссылку. Если он попросит, открывайте PR в учебный репозиторий.

> Важно: без fork и без прав Collaborator отправка `git push` в `tishelka/backend-training` не получится. Для fork используйте адрес **своей** копии при `git clone`.

**Цель:** в конце вы не только знаете названия технологий, а можете самостоятельно собрать небольшой CRUD API и объяснить, откуда пришёл JSON, как он проверился и почему запись оказалась в PostgreSQL.
