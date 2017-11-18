#!/bin/bash
sudo /etc/init.d/mysql start

mysql -uroot -e "create user 'django-app' identified by '111111'"
mysql -uroot -e "create database qa"
mysql -uroot -e "grant all on qa.* to 'django-app'"

./ask/manage.py migrate
