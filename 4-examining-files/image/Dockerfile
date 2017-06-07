FROM python:3.5

RUN pip install Flask gunicorn

RUN useradd my-app

ADD hello.py /app/hello.py
WORKDIR /app

RUN touch /var/log/my-app-access.log && chown my-app:my-app /var/log/my-app-access.log

CMD su -c "cd /app ; gunicorn --access-logfile=/var/log/my-app-access.log hello:app" - my-app
