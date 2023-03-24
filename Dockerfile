FROM python:3.10.0b1

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

RUN mkdir /backend
WORKDIR /backend
COPY ./backend/ /backend
RUN mkdir /backend/backend/static

# RUN adduser -D user
# USER user
