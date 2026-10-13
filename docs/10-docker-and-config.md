# 10. Docker, настройки и ошибки

`Dockerfile` создаёт образ нашего Python-сервера. `compose.yaml` запускает две службы — PostgreSQL и FastAPI. Это помогает запускать одинаковое окружение на компьютерах команды.

```bash
docker compose up --build -d
docker compose ps
docker compose logs api
```

Остановка: `docker compose down`. Для сохранения данных используется Docker volume. Не используйте команды удаления volume, если хотите сохранить учебную БД.

**Разница адресов:** Python на ноутбуке обращается к PostgreSQL по `localhost:5432`. Контейнер API обращается по `db:5432` — `db` это имя службы в Compose.

### Конфигурация

В реальном MVP используется **Pydantic Settings**:

```python
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    database_url: str
```

Создайте локальный `.env` по образцу `.env.example`; не добавляйте его в Git. Проверяйте настройки до запуска приложения.

### Ошибки

`404` — не найдено, `422` — неверный формат запроса, `409` — конфликт данных, `503` — временная недоступность БД. Возвращайте понятные сообщения без пароля, полного SQL и stack trace.

Наш учебный API не требует авторизации, поэтому **не публикуйте его в открытый интернет**.

[Вернуться в README](../README.md).
