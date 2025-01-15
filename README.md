# mellow-skunk
django-rest application for mellow collectors, shares the results of the most recent collection cycle via REST and exposes simple prometheus statistics.  One instance of mellow-skunk should be active on every collection host.

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