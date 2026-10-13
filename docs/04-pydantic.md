# 04. Pydantic v2: когда клиент прислал ерунду

Мобильное приложение может ошибиться: прислать отрицательную цену, строку вместо числа, неизвестную категорию. Проверять это лучше **на границе API**, а не после записи в БД.

```python
from pydantic import BaseModel, Field

class ActivityCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    cost: int = Field(ge=0)
    duration_minutes: int = Field(gt=0)
```

```python
@app.post("/activities")
def create_activity(activity: ActivityCreate):
    return activity
```

FastAPI возьмёт JSON из тела запроса, передаст Pydantic, а при некорректных полях вернёт **422** с описанием ошибки. Попробуйте `{"title":"Прогулка","cost":-50,"duration_minutes":60}` и посмотрите результат через Swagger.

**Полезное разделение:** схема запроса (`ActivityCreate`) и схема ответа (`ActivityOut`) могут отличаться. Клиент не должен сам выбирать служебные ID и даты создания, если это ответственность сервера.

В реальном MVP «ЧтоДальше» используется `Pydantic v2` с `Field`, `field_validator`, `model_validator` и преобразованием JSON-полей **snake_case → camelCase**. Например, Python `duration_minutes` соответствует JSON `durationMinutes`. Для этого есть `alias_generator` из `pydantic.alias_generators`. Потренируйтесь сначала с обычными именами полей.

**Дополнительный вопрос:** что должно случиться, если клиент передал неизвестное поле? Для строгой схемы изучите `ConfigDict(extra="forbid")`.

[Практика 03](../exercises/03-validation.md).
