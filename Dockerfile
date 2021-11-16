FROM python:3.10

RUN pip install uwsgi==2.0.20

EXPOSE 8080
CMD ["uwsgi", "uwsgi.ini"]

RUN mkdir app
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ARG data_path=/app/data

VOLUME ["$data_path"]
ENV SCHEDULER_DB="sqlite:///$data_path/apscheduler.db"
ENV TIMEZONE="Europe/Madrid" LOG_LEVEL="INFO"

# Se copian los ficheros por frecuencia de modificación: de menos a más
COPY wsgi_app.py .

COPY scheduler ./scheduler/
COPY uwsgi.ini .
