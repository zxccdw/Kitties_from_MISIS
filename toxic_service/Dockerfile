# Используем базовый образ Python
FROM python:3.12-slim

# Устанавливаем нужные зависимости
RUN pip install --no-cache-dir fastapi uvicorn transformers torch

# Задаем рабочую директорию в контейнере
WORKDIR /app

# Скачиваем модель на этапе сборки контейнера
RUN python -c "from transformers import AutoTokenizer, AutoModelForSequenceClassification; \
               AutoTokenizer.from_pretrained('cointegrated/rubert-tiny-toxicity').save_pretrained('./rubert-tiny-toxicity'); \
               AutoModelForSequenceClassification.from_pretrained('cointegrated/rubert-tiny-toxicity').save_pretrained('./rubert-tiny-toxicity')"

# Копируем приложение в контейнер
COPY ./main.py /app/main.py

# Задаем команду для запуска приложения при старте контейнера
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
