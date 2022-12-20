FROM python:3.11.1-slim-buster AS base_build

ENV \
  # python:
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PYTHONDONTWRITEBYTECODE=1 \
  # pip:
  PIP_NO_CACHE_DIR=1 \
  PIP_DISABLE_PIP_VERSION_CHECK=1 \
  PIP_DEFAULT_TIMEOUT=100 \
  # poetry:
  POETRY_VERSION=1.3.1 \
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry' \
  POETRY_HOME='/usr/local'

RUN apt-get update && apt-get upgrade -y \
  && apt-get install --no-install-recommends -y \
    bash \
    curl \
  # Installing `poetry` package manager:
  # https://github.com/python-poetry/poetry
  && curl -sSL 'https://install.python-poetry.org' | python - \
  && poetry --version \
  # Cleaning cache:
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && apt-get clean -y && rm -rf /var/lib/apt/lists/*

WORKDIR /src

# Copy only requirements, to cache them in docker layer
COPY ./src/poetry.lock ./src/pyproject.toml /src/

# Project initialization:
RUN poetry version \
  # Install deps:
  && poetry run pip install -U pip \
  && poetry install --only main --no-interaction --no-ansi \
  && rm -rf ~/.cache/pypoetry/{cache,artifacts}

FROM base_build as development_build

RUN poetry install --with dev --no-interaction --no-ansi \
    && rm -rf ~/.cache/pypoetry/{cache,artifacts}

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]

FROM base_build as production_build

COPY  . /src

CMD ["/src/start.sh"]
