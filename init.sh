#!/bin/bash

sudo ln -sf "$(pwd)/etc/nginx.conf"  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx reload

sudo ln -sf "$(pwd)/etc/hello.py" /etc/gunicorn.d/hello.py
gunicorn -c /etc/gunicorn.d/hello.py --chdir "$(pwd)/web" hello:app &
