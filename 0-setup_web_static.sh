#!/usr/bin/env bash
# configure my servers

apt-get -y update
apt-get -y install nginx
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared
echo "test wowww" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -hR ubuntu:ubuntu /data
n="server_name _;\n     location \/hbnb_static\/ {\n\talias \/data\/web_static\/current\/; \n\t}"
sed -i "s/server_name _;/$n/" /etc/nginx/sites-available/default
service nginx restart
