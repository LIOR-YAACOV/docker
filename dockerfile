FROM python:3.11-slim

WORKDIR /app

COPY first_app.py /app/
COPY config.json /app/
COPY requirements.txt /app/
COPY printColors.py /app/

RUN pip install -r requirements.txt

ENV HOST_IP=0.0.0.0

EXPOSE 80

CMD ["python", "first_app.py"]