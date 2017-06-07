FROM python:3.5

RUN pip install Flask gunicorn

RUN useradd my-app

ADD hello.py /app/hello.py
WORKDIR /app

CMD su -c "cd /app ; gunicorn hello:app" - my-app
