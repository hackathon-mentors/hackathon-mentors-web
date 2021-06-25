FROM python:3.8.2
ENV PYTHONUNBUFFERED 1

RUN mkdir /api
WORKDIR /api

RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -
RUN apt-get install -y apt-utils
RUN apt-get install -y nodejs

COPY requirements.txt /api
RUN pip install -r requirements.txt

COPY hackathonmentors /api
COPY . /api/

CMD gunicorn -b :8000 hackathonmentors.wsgi
