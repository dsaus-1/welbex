FROM python:3.10.11-buster

WORKDIR /code

COPY . .

RUN curl -sSL https://install.python-poetry.org | python3.10 -

ENV PATH="/root/.local/bin:$PATH"
RUN poetry config virtualenvs.create false \
    && poetry install


