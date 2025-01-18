# mellow-skunk
Mellow Skunk is a [django-rest](https://www.django-rest-framework.org/) application for mellow collectors such as [mellow-heeler](https://github.com/guycole/mellow-heeler) and [mellow-hyena](https://github.com/guycole/mellow-hyena).  Mellow Skunk provides a easy mechanism to share the most recent results of a collection cycle.  Mellow Skunk also exposes collection metrics to [prometheus](https://prometheus.io/) by using [django-prometheus](https://github.com/korfuri/django-prometheus).

There is only one skunk instance per host and it exposes statistics for all collection operations on the host.

## deployment
![deployment](https://github.com/guycole/mellow-skunk/blob/main/md_url/deployment.png)

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
1. Verify you can run mellow skunk with gunicorn
    + ```gunicorn --bind 0.0.0.0:8000 mellow.wsgi```
1. Configure systemd(1) to invoke gunicorn
    + ```cd ..;ls``` (you should see two gunicorn.* files)
    + ```sudo cp gunicorn.* /etc/systemd/system```
    + ```sudo systemctl start gunicorn.socket```
    + ```sudo systemctl enable gunicorn.socket```
    + ```sudo systemctl status gunicorn.socket```
    + ```curl -v --unix-socket /run/gunicorn.sock localhost```
        + should see a JSON payload from skunk
    + ```sudo systemctl status gunicorn```
1. Configure nginx(8) reverse proxy
    + Install nginx(8) if not already present
        + ```sudo apt-get install nginx```
    + ```cp reverse-proxy.conf /etc/nginx/sites-available```
    + ```ln /etc/nginx/sites-available/reverse-proxy.conf /etc/nginx/sites-enabled```
    + ```rm /etc/nginx/sites-enabled/default```
    + ```sudo systemctl restart nginx```
1. mellow-skunk should now be responding at ```http://localhost```

## configuration
1. Define the host.
    + Example [curl-host-rpi3d-post.sh](https://github.com/guycole/mellow-skunk/blob/main/bin/curl-host-rpi3d-post.sh)
1. Define a task.
    + Example [curl-task-heeler-post.sh](https://github.com/guycole/mellow-skunk/blob/main/bin/curl-task-heeler-post.sh)

## URL
| URL       | Verb      | Payload                         |
| --------- | ----------|-------------------------------- |
| /heeler/  | get, post | JSON [Example](https://github.com/guycole/mellow-skunk/blob/main/bin/curl-heeler-test-post.sh) |
| /host     | get, post | JSON                            |
| /hyena/   | get, post | JSON [Example](https://github.com/guycole/mellow-skunk/blob/main/bin/curl-hyena-test-post.sh)  |
| /groups   | get       | JSON                            |
| /metrics  | get       | Prometheus Text [Example](https://github.com/guycole/mellow-skunk/blob/main/scrape.txt)|
| /task/    | get, post | JSON                            |
| /users    | get, post | JSON                            |

## Relevant Links
+ [django, nginx, gunicorn](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu#step-7-creating-systemd-socket-and-service-files-for-gunicorn)
+ [django prometheus](https://github.com/korfuri/django-prometheus)
+ [django rest example](https://www.geeksforgeeks.org/how-to-create-a-basic-api-using-django-rest-framework/)
+ [django rest tutorial](https://www.django-rest-framework.org/tutorial/1-serialization/)
+ [django rest repository](https://github.com/encode/django-rest-framework)
+ [monitor django w/prometheus](https://blog.snapdragon.cc/posts/2022-12-monitor-django-with-prometheus/)
+ [python client_python](https://github.com/prometheus/client_python)
