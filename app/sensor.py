import os
from dagster import sensor, RunRequest
import pandas as pd
from sqlalchemy import create_engine


@sensor(pipeline_name="sensor_pipeline", minimum_interval_seconds=30)
def my_sensor():
    USER = 'test_user'
    PW = 'test_user'
    table = 'test_table'

    engine = create_engine(f'postgresql://{USER}:{PW}@postgre:5432/test_user')
    df = pd.read_sql(sql=f'select * from {table}', con=engine)

    if len(df) == 0:
        pass
    else:
        yield RunRequest(run_key=None, run_config={})
