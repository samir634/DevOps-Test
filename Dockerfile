FROM python:3.7-alpine
WORKDIR /code
RUN pip install influxdb
COPY app.py app.py
CMD ["python", "./app.py"]