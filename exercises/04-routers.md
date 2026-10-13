# Задание 04. Переносим маршруты в APIRouter

**Теория:** [APIRouter и Depends](../docs/05-routers-and-dependencies.md).

Вынесите маршруты активностей из `app/main.py` в `app/routers/activities.py`. Добавьте `app/routers/__init__.py`. В `main.py` пусть останутся создание `FastAPI`, `health` и `include_router`.

**Дополнительно:** создайте зависимость `get_default_limit` с `Depends`, которая пока просто возвращает 10. Используйте её для параметра пагинации, а затем объясните, почему позднее аналогично можно передавать SQLAlchemy Session.

**Проверка:**
- `GET /health` всё ещё работает.
- `GET /activities` и `POST /activities` видны в Swagger.
- Плохое значение limit даёт 422, как прежде.
- Запустили `pytest` и `ruff`.

**Зачем:** добавление новых групп `/favorites` и `/history` не должно превращать `main.py` в огромный файл.
