FROM python:3.10.0b1

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

RUN mkdir /backend
RUN mkdir /backend/static
RUN mkdir /backend/media
WORKDIR /backend
COPY . /backend/


CMD sh -c "python manage.py wait_for_db && \
             python manage.py migrate && \
             gunicorn backend.wsgi:application --bind 0.0.0.0:8000"