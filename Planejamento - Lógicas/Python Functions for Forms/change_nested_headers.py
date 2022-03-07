
import pandas as pd

# Function Change headers 
def _fn(metadata):
    metadata['nestedHeaders'][0] = aux__trocar_nested_headers_moinhos # Example datas [''2021-06, 2021-07 ....]
    return metadata
result = _fn

# Nested columns receive new index.
_n = 144
nestedHeaders = {}
_df = pd.DataFrame({'label':[f'Period_{i:03d}' for i in range(1, _n+1)]})
_df['colspan'] = 6

_list = _df.to_dict('record')

nestedHeaders['nestedHeaders'] = _list
print(nestedHeaders)

