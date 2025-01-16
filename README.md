# mellow-skunk
Mellow Skunk is a [django-rest](https://www.django-rest-framework.org/) application for mellow collectors such as [mellow-heeler](https://github.com/guycole/mellow-heeler) and [mellow-hyena](https://github.com/guycole/mellow-hyena).  Mellow Skunk provides a easy mechanism to share the most recent results of a collection cycle.  Mellow Skunk also exposes collection metrics to [prometheus](https://prometheus.io/) by using [django-prometheus](https://github.com/korfuri/django-prometheus).

## deployment
Mellow collector hosts are all based on [Raspberry Pi](https://en.wikipedia.org/wiki/Raspberry_Pi).
The mellow skunk application is distributed via github and expected to reside at ```/home/gsc/Documents/github/mellow-skunk```, and this path is hard coded in many scripts.

The django-rest application executes from gunicorn invoked by systemd(1), and should always be available.  

nginx(8) acts as a reverse proxy to gunicorn and is also started by systemd(1), and should always be available.

## operation
Once mellow skunk has been installed and configured, the collection applications can post a JSON payload for each collection cycle.  All previous results will be deleted and only the freshest content will be retained.  Also, the prometheus gauge for collection population will be updated.  The uploaded content can be reviewed w/a GET at the URL below.

## installation
1. Clone mellow skunk repo within ```/home/gsc/Documents/github```
    + Scripts are expecting application at ```/home/gsc/Documents/github/mellow-skunk```
1. Establish python environment
    + ```cd mellow-skunk/src/django-rest```
    + Invoke virtualenv, i.e. ```virtualenv -p /usr/local/opt/python@3.9/bin/python3.9 venv```
    + ```source venv/bin/activate```
    + ```pip install -r requirements.txt```
1. Verify you can start django
    + ```cd mellow```
    + ```python manage.py migrate```
    + ```python manage.py runserver```


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