from django.apps import AppConfig

class SkunkConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "skunk"

from prometheus_client import (
    CollectorRegistry,
    Counter,
    Gauge,
    Histogram,
    generate_latest,
)

registry = CollectorRegistry()

HYENA_OBS_GAUGE = Gauge(
    'hyena_obs_gauge',
    'current hyena observation population',
)

HEELER_OBS_GAUGE = Gauge(
    'heeler_obs_gauge',
    'current heeler observation population',
)

def registry_to_text():
    return generate_latest(registry)

