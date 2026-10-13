# 09. Pytest, HTTPX и Ruff: проверяем себя

В Swagger удобно запускать запросы руками, но после каждого изменения лучше иметь **автоматические проверки**.

```bash
python -m pytest -q
python -m ruff check .
```

Стартовый `tests/test_health.py` уже проверяет `GET /health` и наличие маршрута в OpenAPI.

```python
from fastapi.testclient import TestClient
from app.main import app

def test_health():
    response = TestClient(app).get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
```

TestClient использует HTTPX; настоящий сервер Uvicorn для него запускать не нужно. По мере развития сервиса добавляйте проверки `404`, `422`, создания, изменения и повторной отправки запросов.

Для тестов с сохранением данных выделяйте **отдельную тестовую БД**. Никогда не запускайте тесты, которые меняют данные, на общей рабочей базе.

`Ruff` — быстрая проверка импорта и основных ошибок. Исправляйте предупреждения осознанно, а не подавляйте всё подряд.

[Практика 08](../exercises/08-tests.md).
