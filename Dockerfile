FROM python:alpine
COPY app.py /app.py
COPY lib /lib
ENTRYPOINT ["python", "app.py"]