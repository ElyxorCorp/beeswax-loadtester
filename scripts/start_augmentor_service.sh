sudo docker run -d -p 8085:8080 -v /var/log/loadtester:/var/log/loadtester -e BEESWAX_AUTH_SECRET=VERY_SECURE_SECRET --name beeswax-loadtester beeswax-loadtester:1.0
