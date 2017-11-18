# Stepik Web Dev

The repository for storing exercies in web-development course

## Prerequisites

1. Install docker

    ```
    sudo curl -sSL https://get.docker.com/ | sh && sudo gpasswd -a ${USER} docker
    ```

1. [Install docker-compose](https://github.com/docker/compose/releases)

1. Logout and login

## Getting started

1. Migrate database

    ```bash
    docker-compose run --rm backend ./ask/manage.py migrate
    ```

1. Run app

    ```bash
    docker-compose up
    ```
