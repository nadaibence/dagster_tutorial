from dagster import pipeline, solid
import pandas as pd
from sqlalchemy import create_engine
import random


@solid
def extract():
    a = random.choice(range(100))
    data = [[a,a,a],
            [a,a,a],
            [a,a,a]]
    columns = ['A', 'B', 'C']
    
    df = pd.DataFrame(data=data, columns=columns)
    return df


@solid
def transform(df):
    df['D'] = 'user'
    df['E'] = 'test'
    return df
    

@solid
def load(df):
    USER = 'test_user'
    PW = 'test_user'
    table = 'test_table'

    engine = create_engine(f'postgresql://{USER}:{PW}@postgre:5432/test_user')
    df.to_sql(name=table, con=engine, if_exists='append', index=False)


@pipeline
def etl_pipeline():
    e = extract()
    t = transform(e)
    load(t)