#!/bin/bash

gunicorn -c "$(pwd)/etc/hello.py" --chdir "$(pwd)/web" hello:app &
sudo ln -sf "$(pwd)/web/etc/nginx.conf"  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
