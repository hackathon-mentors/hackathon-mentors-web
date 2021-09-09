# hackathonmentors-web

Website for Hackathon Mentors

## Requirements

- UNIX environment (Windows users look into WSL2)
- Python 3.8.2 or higher
- [docker](https://www.docker.com/get-started) ([WSL2](https://docs.docker.com/docker-for-windows/wsl/) reference)
- docker-compose

## Setup

1. Clone into this repository:
  ```shell
  $ git clone https://github.com/hackathon-mentors/hackathon-mentors-web.git
  ```

2. In the repository's root directory, create a directory named `secrets` and make a `django_secret` file to create your own [Django secret key](https://docs.djangoproject.com/en/3.0/ref/settings/#secret-key).

  ```shell
  $ cd hackathon-mentors-web 
  $ mkdir secrets && cd secrets
  $ cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 50 | head -n 1 > django_secret
  ```

  (Note: for macOS, the last command may not run and shell would complain about `tr: Illegal byte sequence` error. Use the following instead:


  ```shell
  $ cat /dev/urandom | LC_ALL=C tr -dc 'a-zA-Z0-9' | fold -w 50 | head -n 1 > django_secret
  ```

  Use the following template to create `db.env` in `secrets` folder, using your preferred text editor:

  ```shell
  POSTGRES_DB=hackathonmentors
  POSTGRES_USER=hackathonmentors_user
  POSTGRES_PASSWORD=hackathonmentors_pass
  ```

3. Run `docker-compose up -d` to start building & spinning up the `web` and `db` images.
  - Since we are running docker-compose v3, the db may come up before the web server.
  - Check logs `docker-compose logs -f web` and see if it has connection errors.
  - If so, simply do `docker-compose restart web`
4. `docker-compose exec web bash` to go into the django (web) image:
  - `python hackathonmentors/manage.py migrate` to set up initial database
  - `python hackathonmentors/manage.py createsuperuser` to create an admin user for your localhost.
  - `python hackathonmentors/manage.py loaddata hackathonmentors/hackathon/fixtures/0001_initial.json` to load up sample hackathon data (from [HackathonScraper](https://github.com/hackathon-mentors/HackathonScraper)!)
     NOTE: The fixture will be bind the sample hackathon objects' creator as the first user (i.e. `id=1`) you created from running the `createsuperuser` command from above.
  - Run `UPDATE django_site SET domain='127.0.0.1', name='127.0.0.1' WHERE id='1';` in the SQL database to expose the site locally.
5. Visit [http://localhost:8000/](http://localhost:8000/) :sparkles:

## Deployment

Production deployment is separate from using `docker-compose`:

```shell
$ docker build . -t web  # to build a docker image
$ docker tag web hm-web:<version>  # (check version at https://github.com/hackathon-mentors/hackathon-mentors-web/blob/master/k8s/hm.yaml)
$ docker push hm-web:<version>  # to push up to docker hub
```

_NOTE: more deployment info to be added once we go prod_
