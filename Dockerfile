FROM python:3.11-slim

# Установка необходимых пакетов
RUN apt-get update && apt-get install -y curl libpq-dev build-essential

# Установка Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Настройка переменной PATH
ENV PATH="/root/.local/bin:$PATH"

# Установка рабочей директории
WORKDIR /app

# Копирование файлов для Poetry
COPY pyproject.toml poetry.lock ./

# Установка зависимостей через Poetry
RUN poetry install --no-root

# Копирование всех файлов проекта
COPY . .

# Установка прав на выполнение скриптов
RUN chmod a+x /app/docker/*.sh

# Проверка установки alembic и gunicorn
RUN /root/.local/bin/poetry run alembic --version
RUN /root/.local/bin/poetry run gunicorn --version