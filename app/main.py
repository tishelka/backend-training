"""Старт курса. Новые маршруты добавляйте сами, по заданиям."""
from fastapi import FastAPI

app = FastAPI(title="Учебный каталог идей", version="0.1.0")


@app.get("/health", tags=["Состояние"], summary="Проверить, что API работает")
def health() -> dict[str, str]:
    return {"status": "ok"}
