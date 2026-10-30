FROM python:3.12-slim

WORKDIR /app

# show print() output immediately in docker logs
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
