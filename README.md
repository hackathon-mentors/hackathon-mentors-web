# hackathonmentors-web

Website for Hackathon Mentors

## Requirements

- Python 3.8.2 or higher
- docker
- docker-compose

## Setup

1. Create `secrets` folder and place `db.env` and `django_secret` in there (get this from [@hunj](https://github.com/hunj).
2. `docker-compose up`
3. Visit [http://localhost:8000/](http://localhost:8000/)

## Deployment

Deployment for MVP v1 is done on Heroku using branch `prod-heroku`. Check `/heroku.yml` within.
