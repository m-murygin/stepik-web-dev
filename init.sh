#!/bin/bash

gunicorn -c /home/box/etc/hello.py --chdir /home/box/web hello:app
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
