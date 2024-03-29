FROM python:alpine3.7

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 8000

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8000"]