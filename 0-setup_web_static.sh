#!/usr/bin/env bash
# some configdd

apt-get -y update
apt-get install nginx
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "test" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
n="server_name _;\n     location \/hbnb_static { \n         alias \/data\/web_static\/current\/; \n      }"
sed -i "s/server_name _;/$n/" /etc/nginx/sites-available/default
service nginx restart
