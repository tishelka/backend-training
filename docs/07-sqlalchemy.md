# 07. SQLAlchemy + psycopg: Python и PostgreSQL

`psycopg 3` подключает Python к PostgreSQL, а `SQLAlchemy 2` помогает описывать таблицы классами и выполнять запросы.

```python
from sqlalchemy import create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

class Base(DeclarativeBase):
    pass

class Note(Base):
    __tablename__ = "notes"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]

engine = create_engine("postgresql+psycopg://training:training@localhost:5432/training")

with Session(engine) as session:
    notes = session.scalars(select(Note)).all()
```

**Важно:** класс описывает модель, но сам по себе таблицу в базе не создаёт. На этапе эксперимента есть `Base.metadata.create_all(engine)`, но для настоящей истории изменений используйте Alembic.

Чтобы сохранить новый объект, применяются `session.add(...)` и `session.commit()`. После ошибки обычно требуется `session.rollback()`. Не пишите реальные пароли в Python-файлах: получайте строку подключения из окружения.

В «ЧтоДальше» используются **синхронные** SQLAlchemy Session и обычные `def`-обработчики FastAPI. Позже сессию удобно передавать маршрутам через `Depends`: один запрос — одна управляемая сессия.

[Практика 06](../exercises/06-crud.md).
