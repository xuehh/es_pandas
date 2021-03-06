import time

import pandas as pd

from es_pandas import es_pandas


# Information of es cluseter
es_host = 'localhost:9200'
index = 'demo'

# crete es_pandas instance
ep = es_pandas(es_host)

# Example data frame
df = pd.DataFrame({'Alpha': [chr(i) for i in range(97, 128)],
                    'Num': [x for x in range(31)],
                    'Date': pd.date_range(start='2019/01/01', end='2019/01/31')})

# init template if you want
doc_type = 'demo'
ep.init_es_tmpl(df, doc_type, delete=True)

# Example of write data to es
ep.to_es(df, index, doc_type=doc_type, use_index=True)

# waiting for es data writing
time.sleep(5)
ep.delete_es(df.iloc[0:10, :], index)

# waiting for es data writing
time.sleep(5)
# get certain fields from es, set certain columns dtype
heads = ['Num', 'Date', 'Alpha']
dtype = {'Num': 'float', 'Alpha': object}
df = ep.to_pandas(index, heads=heads, dtype=dtype)
print(df.head())
print(df.dtypes)

# infer dtypes from es template
df = ep.to_pandas(index, infer_dtype=True)
print(df.dtypes)
