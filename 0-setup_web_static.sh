#!/usr/bin/env bash
# Bash scrip to set up web servers to deploy web_static

# install nginx if not exist
sudo apt-get update
sudo apt-get -y install nginx

# create directory: data, web_static, shared
sudo mkdir -p /data/web_static/shared/

# Using -p flag, we want to ensure that the following directory exist before creating /test
sudo mkdir -p /data/web_static/releases/test/

# put the following html code in the index.html 
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# reate a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Giving ownership of the /data/ folder to the ubuntu user AND group (assuming this user and group exist)
sudo chown -R ubuntu:ubuntu /data

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sudo sed -i '53i \\tlocation \/hbnb_static {\n\t\t alias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default

# restart nginx
sudo service nginx restart
