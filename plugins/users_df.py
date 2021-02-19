import pandas as pd
from sqlalchemy import create_engine


class DFGenerator:
    def __init__(self):
        self.engine = create_engine(
            'postgres://tujgeuwousxogt:3cd93f7ae944317d4437ae3ee94d9937202dd6696d79a6a3947f99e4fe6de964@ec2-54-144-251-233.compute-1.amazonaws.com:5432/dpjqsrful94gn')
        self.df = pd.read_sql(sql='SELECT * FROM users', con=self.engine, index_col='id')

    def save(self):
        self.df.to_sql(name='users', con=self.engine, if_exists='replace', index_label='id')
