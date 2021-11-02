from dagster import pipeline, solid, repository

from sensor import my_sensor
from sensor_pipeline import sensor_pipeline
from tutorial import etl_pipeline
from schedule import good_morning_schedule

@repository
def test_repository():
    return [
        etl_pipeline,
        sensor_pipeline,
        my_sensor,
        good_morning_schedule
    ]