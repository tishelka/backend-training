# 06. PostgreSQL: постоянные данные

Список Python пропадёт после перезапуска сервера. В PostgreSQL данные лежат в таблицах и переживают рестарт приложения.

Запустите Docker Desktop:

```bash
docker compose up -d db
docker compose exec db psql -U training -d training
```

Создадим **отдельную учебную таблицу** прямо в psql:

```sql
CREATE TABLE practice_notes (
  id SERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  done BOOLEAN NOT NULL DEFAULT FALSE
);
INSERT INTO practice_notes (title) VALUES ('Разобраться с SQL');
SELECT id, title, done FROM practice_notes;
UPDATE practice_notes SET done = TRUE WHERE id = 1;
```

Выйти из psql: `\q`. Таблицы состоят из столбцов и строк. `PRIMARY KEY` — уникальный ключ строки; `FOREIGN KEY` — ссылка на строку другой таблицы; `NOT NULL` не разрешает пропущенное значение; `UNIQUE` предотвращает дубли.

Две важные идеи: **схема БД** — это структура таблиц, **данные БД** — значения внутри строк. Первую в проекте меняет Alembic, вторые — обычные SQLAlchemy-запросы.

Локальные реквизиты курса: база и пользователь `training`, пароль `training`. Это демонстрационные значения, не используйте их в публичной системе.

[Практика 05](../exercises/05-postgres.md).
