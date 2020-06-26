# hackathonmentors-web

Website for Hackathon Mentors

## Requirements

- Python 3.8.2 or higher
- docker
- docker-compose

## Setup

1. Create `secrets` folder and place `db.env` and `django_secret` in there (get these files from [@hunj](https://github.com/hunj)).
2. `docker-compose up -d` to start building.
3. `docker-compose exec web bash` to go into the django image:
  - `python hackathonmentors/manage.py migrate` to set up initial database
  - `python hackathonmentors/manage.py createsuperuser` to create an admin user for your localhost.
4. Visit [http://localhost:8000/](http://localhost:8000/)

## Deployment

Production deployment is separate from using `docker-compose`:

```shell
$ docker build . -t web  # to build a docker image
$ docker tag web hm-web:<version>  # (check version at https://github.com/hackathon-mentors/hackathon-mentors-web/blob/master/k8s/hm.yaml)
$ docker push hm-web:<version>  # to push up to docker hub
$ # change version name in the k8s file from step 2 & save that file
$ kubectl deploy -f hm.yaml
```

