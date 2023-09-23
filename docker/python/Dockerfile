#python 3.8.17
FROM python:3.8

WORKDIR /var/www/project

COPY ./pyproject.toml /var/www/project/pyproject.toml
COPY ./poetry.lock /var/www/project/poetry.lock

ENV PYTHONPATH /var/www/project/src/handlers:/var/www/project/src/UseCases

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry install --no-root

COPY ./src /var/www/project/src

CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "6030", "--reload"]