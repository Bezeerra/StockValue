FROM python:3.10

WORKDIR /code

RUN cat > /code/.env

COPY ./requirements.txt /code/requeriments.txt

RUN pip install --no-cache-dir --upgrade -r /code/requeriments.txt

COPY ./main /code/app

#CMD ["uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "8000"]

