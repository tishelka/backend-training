# 11. Seed, upsert и реальный backend «ЧтоДальше»

**Seed** — первоначальная загрузка каталога. **Upsert** — вставка или обновление записи по устойчивому ключу без дублирования. Это удобно для каталога из 70 активностей: повторный запуск приложения не должен создавать ещё 70 одинаковых записей.

В MVP исходный каталог хранится в TypeScript, генератор создаёт `backend/data/activities.json`, а `backend/app/seed.py` читает JSON, проверяет Pydantic и загружает записи в PostgreSQL через `INSERT ... ON CONFLICT`.

| Файл настоящего проекта | Назначение |
| --- | --- |
| [main.py](https://github.com/tishelka/chtodalshe/blob/master/backend/app/main.py) | FastAPI, подключение роутеров, обработчики ошибок |
| [schemas.py](https://github.com/tishelka/chtodalshe/blob/master/backend/app/schemas.py) | Pydantic-схемы, camelCase |
| [database.py](https://github.com/tishelka/chtodalshe/blob/master/backend/app/database.py) | Engine, Session, Depends |
| [models.py](https://github.com/tishelka/chtodalshe/blob/master/backend/app/models.py) | Таблицы SQLAlchemy |
| [routers/](https://github.com/tishelka/chtodalshe/tree/master/backend/app/routers) | Каталог, настройки, избранное, история |
| [seed.py](https://github.com/tishelka/chtodalshe/blob/master/backend/app/seed.py) | Наполнение каталога |
| [bootstrap.py](https://github.com/tishelka/chtodalshe/blob/master/backend/app/bootstrap.py) | Миграции и seed |
| [migrations/](https://github.com/tishelka/chtodalshe/tree/master/backend/migrations) | Изменения схемы PostgreSQL |

В текущем MVP все клиенты работают с **одним общим профилем**, нет регистрации и токенов; доступ к изменениям общего профиля не ограничен учётными записями. Рекомендательный движок остаётся **на мобильном клиенте в TypeScript**, не на FastAPI.

**Задание на понимание:** проследите GET `/activities` через `main.py` → `routers/activities.py` → `database.py` → `models.py` → Pydantic `schemas.py`. Сможете объяснить каждую стрелку своими словами?

[К началу курса](../README.md).
