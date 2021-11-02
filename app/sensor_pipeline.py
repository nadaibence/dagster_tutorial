from dagster import pipeline, solid
import pandas as pd
from sqlalchemy import create_engine


@solid
def extract_a():
    USER = 'test_user'
    PW = 'test_user'
    table = 'test_table'

    engine = create_engine(f'postgresql://{USER}:{PW}@postgre:5432/test_user')
    df = pd.read_sql(sql=f'select * from {table}', con=engine)
    return df


@solid
def transform_a(df):
    df['F'] = 'HEY'
    df['G'] = 'HO'
    return df
    

@solid
def load_a(df):
    USER = 'test_user'
    PW = 'test_user'
    table = 'test_sensor'

    engine = create_engine(f'postgresql://{USER}:{PW}@postgre:5432/test_user')
    df.to_sql(name=table, con=engine, if_exists='replace', index=False)


@pipeline
def sensor_pipeline():
    e = extract_a()
    t = transform_a(e)
    load_a(t)