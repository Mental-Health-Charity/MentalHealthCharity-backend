FROM python:3.9

WORKDIR /workdir/

ENV YOUR_ENV=dev \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.5.1

# System deps:
RUN pip install "poetry==$POETRY_VERSION"

# Copy poetry.lock* in case it doesn't exist in the repo

# Copy poetry.lock* in case it doesn't exist in the repo
COPY ./pyproject.toml ./poetry.lock* /workdir/

# Allow installing dev dependencies to run tests
RUN poetry config virtualenvs.create false \
  && poetry install $(test "$YOUR_ENV" == production && echo "--no-dev") --no-interaction --no-ansi

COPY ./ /workdir
ENV PYTHONPATH=/workdir
