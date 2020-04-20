FROM python:3.8.2
ENV PYTHONUNBUFFERED 1

RUN mkdir /build
WORKDIR /build

RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -
RUN apt-get install -y nodejs

COPY requirements.txt /build
RUN pip install -r requirements.txt

RUN groupadd -r django && useradd -r -g django django
COPY . /build
RUN chown -R django /build

COPY hackathonmentors /build
COPY . /build/
