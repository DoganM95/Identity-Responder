FROM python:3.9-slim

WORKDIR /usr/src/app

COPY ./app.py app.py

RUN pip install --no-cache-dir Flask

EXPOSE 8080

CMD ["python", "app.py"]