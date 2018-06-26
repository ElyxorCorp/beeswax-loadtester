sudo docker run -d -p 8089:8089 -v /var/log/loadtester:/var/log/loadtester -e BEESWAX_AUTH_SECRET=SECRET_SO_LEGIT beeswax-loadtester:local --name loadtester loadtester
