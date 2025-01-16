# mellow-skunk
Mellow Skunk is a [django-rest](https://www.django-rest-framework.org/) application for mellow collectors such as [mellow-heeler](https://github.com/guycole/mellow-heeler) and [mellow-hyena](https://github.com/guycole/mellow-hyena).  Mellow Skunk provides a easy mechanism to share the most recent results of a collection cycle.  Mellow Skunk also exposes collection metrics to [prometheus](https://prometheus.io/) by using [django-prometheus](https://github.com/korfuri/django-prometheus).

## deployment
Mellow collector hosts are all based on [Raspberry Pi](https://en.wikipedia.org/wiki/Raspberry_Pi).
The mellow skunk application is distributed via github and expected to reside at ```/home/gsc/Documents/github/mellow-skunk```, and this path is hard coded in many scripts.

The django-rest application executes from gunicorn invoked by systemd(1), and should always be available.  

Nginx acts as a reverse proxy to gunicorn and is also started by systemd(1), and should always be available.

## installation


stuff

, shares the results of the most recent collection cycle via REST and exposes simple prometheus statistics.  One instance of mellow-skunk should be active on every collection host.

## GET
+ things

## POST
+ more things

## Relevant Links
+ [django rest tutorial](https://www.django-rest-framework.org/tutorial/1-serialization/)
+ [django rest repository](https://github.com/encode/django-rest-framework)


https://github.com/prometheus/client_python
https://github.com/korfuri/django-prometheus
https://blog.snapdragon.cc/posts/2022-12-monitor-django-with-prometheus/
https://prometheus.github.io/client_python/instrumenting/gauge/

# HELP hyena_obs_gauge current hyena observation population
# TYPE hyena_obs_gauge gauge
hyena_obs_gauge 0.0
# HELP heeler_obs_gauge current heeler observation population
# TYPE heeler_obs_gauge gauge
heeler_obs_gauge 0.0


https://www.geeksforgeeks.org/how-to-create-a-basic-api-using-django-rest-framework/
https://stackoverflow.com/questions/22881067/django-rest-framework-post-array-of-objects