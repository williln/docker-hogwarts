# docker-hogwarts

Try Docker for yourself by checking out this repository! 

# What to do: 

1. Download [Docker](https://www.docker.com/community-edition#/download)
1. Download [Docker Compose](https://docs.docker.com/compose/install/) (If not on a Mac)
1. Fork this repo into your own GitHub space 
1. Clone this repo onto your own machine 

## Run the project (_Lumos_)

    docker-compose up 

Notice how two services are created: `db_1` and `web_1`. See that migrations run and the server starts. 

## Create a superuser 

In a new tab, run: 

    docker-compose run web --rm ./manage.py createsuperuser

## Create sample data 

Log into the admin at `http://localhost:8000/admin/` and add some content. 

Visit `http://localhost:8000/spells/` to see a list of your data, and `http://localhost:8000/spells/{pk}/` to see a detail view of your data. 

## More ideas 

### Migrations 

Add new features to the `Spell` model, or add a new model or app. 

Run 

    docker-compose run --rm web ./manage.py makemigrations 

And then run 

    docker-compose run --rm web ./manage.py migrate 

### Django Shell (_Apparate_)

Hop into the shell with 

    docker-compose run --rm web ./manage.py shell 

And experiment with poking around by importing a model and running queries on it. 

### Add a new requirement 

Update your requirements file with something like `requests` or another library you love. Stop Docker, then restart with:

    docker-compose up --build 

### See your images (_Imago Revelio_)

    docker images 

### See your running containers (_Continens Revelio_)

    docker container ls 

or 

    docker ps 
    
### Add a volume for your data 

It's helpful in development (and pretty necessary in production) to have your data persist across containers and across coding sessions. Read more about volumes in the [docs](https://docs.docker.com/storage/volumes/). 

To add a data volume to your project, make these changes to `docker-compose.yml`: 

    services:
      db:
        ...
        volumes:
          - postgres_data:/var/lib/postgresql/data/

      web:
        ...

    volumes:
      postgres_data:
      
 First add a `volume` element under your `db` service and name it `postgres_data`. Include the path to where your data will be stored in your container. 
 
 Then, add another element at the same level as `services` called `volumes`, and refer to your `postgres_data` volumes. 
 
 Now you won't need to recreate your superuser and test data every time you shut down your containers. 

### Stop for the day (_Nox_)

    docker-compose down 

# Enrichment exercises 

1. Build your image from scratch and give it a name
1. "Exec" into the Docker container with `docker exec --it` 
1. Stop and restart just the `web` container 
1. Add a new service to `docker-compose.yml`; maybe Redis? 
1. Add tests and run them using `docker-compose run` commands 

# Resources 

- [An Intro to Docker for Djangonauts](https://www.revsys.com/tidbits/brief-intro-docker-djangonauts/)
- [Docker: Useful Command Line Stuff](https://www.revsys.com/tidbits/docker-useful-command-line-stuff/)
- [Docker tutorial](https://docs.docker.com/get-started/) 
- [Docker Compose tutorial](https://docs.docker.com/compose/gettingstarted/)
- [Compose and Django tutorial](https://docs.docker.com/compose/django/)
- [Best Practices for Writing Dockerfiles](https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/)
- [10 Things to Avoid in Docker Containers](https://developers.redhat.com/blog/2016/02/24/10-things-to-avoid-in-docker-containers/) 
- Video: [5 Things About Docker](https://channel9.msdn.com/Shows/5-Things/Episode-12-Five-Things-About-Docker)
- [Docker CheatSheet](https://dockercheatsheet.painlessdocker.com/)
- [Dockerizing Django, UWISGI, and Postgres the Serious Way](http://www.eidel.io/2017/07/10/dockerizing-django-uwsgi-postgres/)
- [Managing Sensitive Data with Docker Secrets](https://docs.docker.com/engine/swarm/secrets/)


This repo uses the [Git Commit Message StyleGuide](https://github.com/slashsBin/styleguide-git-commit-message). 


