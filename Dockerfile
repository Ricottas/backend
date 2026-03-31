FROM python:3.14-slim

WORKDIR /app

# Instalar Poetry de forma tradicional via pip
RUN pip install poetry

# Copiar arquivos de configuração
COPY pyproject.toml poetry.lock* ./

# Instalar dependências
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# Copiar código
COPY ./app /app/app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]