FROM python

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install poetry
WORKDIR /
COPY . .
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8081"]
