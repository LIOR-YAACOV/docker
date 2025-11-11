FROM python:3.11-slim

WORKDIR /app

COPY first_app.py /app/
COPY config.json /app/
COPY requirements.txt /app/

RUN pip install -r requirements.txt

ENV HOST_IP=127.0.0.1

EXPOSE 80

CMD ["python", "first_app.py"]