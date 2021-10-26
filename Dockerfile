FROM python:3.9

EXPOSE 8080

RUN mkdir app
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ARG data_path=/app/data

VOLUME ["$data_path"]
ENV SCHEDULER_DB="sqlite:///$data_path/apscheduler.db"
ENV TIMEZONE="Europe/Madrid" LOG_LEVEL="INFO"

CMD ["uwsgi", "uwsgi.ini"]
COPY wsgi_app.py .

COPY scheduler ./scheduler/
COPY uwsgi.ini .
