#!/usr/bin/env bash
# configure my servers

apt-get -y update
apt-get -y install nginx
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "test wowww" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -hR ubuntu:ubuntu /data
# n="server_name _;\n\tlocation \/hbnb_static\/ {\n\talias \/data\/web_static\/current\/; \n\t}\n"
# sudo sed -i "s/server_name _;/$n/" /etc/nginx/sites-available/default
sed -i "s/^\}$/\tlocation \/hbnb_static\/ \{\n\t\talias \/data\/web_static\/current\/\;\n\t\}\n\}/" /etc/nginx/sites-enabled/default
service nginx restart
