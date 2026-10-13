# 05. APIRouter и Depends: порядок вместо гигантского main.py

Пока есть два маршрута, один файл удобен. Когда появятся активности, история, избранное и настройки, поиск нужной функции станет болью.

`APIRouter` помогает собрать маршруты одной темы в собственном модуле:

```python
# app/routers/activities.py
from fastapi import APIRouter

router = APIRouter(prefix="/activities", tags=["Активности"])

@router.get("")
def list_activities():
    return []
```

В `app/main.py`:

```python
from fastapi import FastAPI
from app.routers import activities

app = FastAPI()
app.include_router(activities.router)
```

`Depends` — механизм для повторно используемых зависимостей. Позже так будем передавать сессию SQLAlchemy. Это лучше, чем в каждом маршруте вручную писать создание/закрытие подключения.

```python
from fastapi import Depends

def get_limit():
    return 10

@app.get("/example")
def example(limit: int = Depends(get_limit)):
    return {"limit": limit}
```

Позже зависимость станет похожа на `def get_db(): ... yield session ...`. В вашем MVP тип `Db` определён через `Annotated[Session, Depends(get_db)]`.

**Зачем всё это:** даже новичку понятно, где искать каталог (`routers/activities.py`) и где подключение к базе (`database.py`).

[Практика 04](../exercises/04-routers.md).
