# 02. FastAPI: первый настоящий обработчик

FastAPI связывает адрес и Python-функцию. Сервер Uvicorn принимает HTTP-запрос и передаёт его вашему приложению.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello(name: str = "друг"):
    return {"message": f"Привет, {name}!"}
```

`GET /hello?name=Аня` вернёт персональное приветствие. Это **query-параметр**. `@app.get("/activities/{activity_id}")` и аргумент `activity_id: int` — уже **path-параметр**: он часть адреса.

Обратите внимание: аннотация `: int` нужна не только редактору — FastAPI попробует проверить введённое значение. `/activities/abc`, если ожидается int, даст 422.

```python
from fastapi import HTTPException

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id != 1:
        raise HTTPException(status_code=404, detail="Не найдено")
    return {"id": item_id, "title": "Прогулка"}
```

Когда работаете над MVP, **не пишите весь код в одной функции**. Маршрут принимает запрос и формирует ответ, а детали хранения можно вынести в другие функции или модули.

**Попробуйте:** поменять тип path-параметра с int на UUID, заглянуть в Swagger и отправить неверное значение.

[Урок 03: Swagger](03-swagger.md) · [Практика 01](../exercises/01-first-api.md)
