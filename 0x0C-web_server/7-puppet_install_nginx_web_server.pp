#redirect nginx
exec {'/usr/bin/env sudo apt-get -y update': }
exec {'/usr/bin/env sudo apt-get -y install nginx': }
exec {'/usr/bin/env echo"Hellow World" > /var/www/html/index.nginx-debian.html': }
exec {'/usr/bin/env sudo sed -i "26i \\\trewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4  permanent;" /etc/nginx/sites-available/default': }
exec {'/usr/bin/env sudo sed -i "27i \\\terror_page 404 /custom_404.html;" /etc/nginx/sites-available/default': }
exec {'/usr/bin/env echo "Ceci n\'est pas une page" > /var/www/html/custom_404.html': }
exec {'/usr/bin/env sudo service nginx start': }
