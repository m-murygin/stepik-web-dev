#!/bin/bash

sudo ln -sf "$(pwd)/etc/nginx.conf"  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx reload

# gunicorn -c "$(pwd)/etc/hello.py" hello:app
gunicorn -c "$(pwd)/etc/ask.py" --chdir "$(pwd)/ask" ask.wsgi
