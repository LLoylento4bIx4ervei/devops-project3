FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

ENV DB_HOST=db
ENV DB_NAME=counter_db
ENV DB_USER=postgres
ENV DB_PASS=secret

EXPOSE 5000
CMD ["python", "app.py"]
