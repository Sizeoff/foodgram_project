FROM python:3.9
WORKDIR /code
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . .
CMD gunicorn foodgram_api.wsgi:application --bind 0.0.0.0:8000