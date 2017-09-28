#!/bin/bash

mysql -uroot -e "create user 'django-app' identified by '111111'";
mysql -uroot -e "create database qa";
mysql -uroot -e "grant all on qa.* to 'django-app'";
