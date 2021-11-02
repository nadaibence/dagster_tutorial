import pandas as pd
from sqlalchemy import create_engine, engine

USER = 'test_user'
PW = 'test_user'
engine = create_engine(f'postgresql://{USER}:{PW}@postgre:5432/test_user')

table = 'test_table'
df = pd.DataFrame(data=[[1,2,3], [4,5,6]], columns=['A', 'B', 'C'])
df.to_sql(name=table, con=engine, if_exists='replace', index=False)

df2 = pd.read_sql(f'select * from {table}', con=engine)
print(df2)