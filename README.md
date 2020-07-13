# DevOps-Test

This repository contains a docker-compose to spin up 3 instances. One is Grafana, one is InfluxDB and the final is to execute a Python script. The Python script collects information 
regarding the load average of the host that it is running on. It then stores it temporarily in a local file until it accumulates a set amount of data. Then it deposits the data into InfluxDB.
The python script also verifies the existence of the required database in InfluxDB. Credentials are hard coded. 

Grafana needs to be configured for the data-source. Docker resolves http://influxdb:8086 to the host internally. The .env file contains the credentials required out of the box to access both
Grafana and InfluxDB. It is possible to have a data-source file loaded for Grafana.

Room for improvement:

Resource constraint didn't seem to do much but are set in the docker-compose to what they should ideally be at. Did not notice an impact when the actual hosts were running. Attempted to add dedicated
subnet and IPV4 addresses but would require additional application level configuration to be useful. CIDR range was set to /28 due to small scale.

Machine that these were tested on:

Intel Core i5-8600k @ 3.60 GHz

8 GB RAM

The docker-compose sets two volumes for each of the applications. 



