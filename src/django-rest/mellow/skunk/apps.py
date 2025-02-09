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

POODLE_HUMIDITY_GAUGE = Gauge(
    'poodle_humidity_gauge',
    'current poodle humidity as percentage',
)

POODLE_TEMPERATURE_GAUGE = Gauge(
    'poodle_temperature_gauge',
    'current poodle temperature in degrees Celsius',
)

POODLE_PRESSURE_GAUGE = Gauge(
    'poodle_pressure_gauge',
    'current poodle pressure in millibars',
)

POODLE_ORIENTATION_PITCH_GAUGE = Gauge(
    'poodle_orientation_pitch_gauge',
    'current poodle orientation pitch in radians',
)

POODLE_ORIENTATION_ROLL_GAUGE = Gauge(
    'poodle_orientation_roll_gauge',
    'current poodle orientation roll in radians',
)

POODLE_ORIENTATION_YAW_GAUGE = Gauge(
    'poodle_orientation_yaw_gauge',
    'current poodle orientation yaw in radians',
)

def registry_to_text():
    return generate_latest(registry)
