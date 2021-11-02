from dagster import daily_schedule, pipeline, repository, solid, schedule
from tutorial import etl_pipeline


@schedule(
    pipeline_name="etl_pipeline",
    cron_schedule="* * * * *",
    name="TestSchedule"
)
def good_morning_schedule():
    return {
        "solids": {
            "extract": {"config": {}},
            "transform": {"config": {}},
            "load": {"config": {}}
        }
    }
