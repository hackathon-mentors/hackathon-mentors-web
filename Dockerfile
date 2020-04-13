FROM python:3.8.2
ENV PYTHONUNBUFFERED 1
COPY hackathonmentors /build
WORKDIR /build
COPY requirements.txt /build
RUN pip install -r requirements.txt
COPY . /build/
