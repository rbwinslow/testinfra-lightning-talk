FROM python:3.5

RUN pip install Flask gunicorn

CMD exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"
