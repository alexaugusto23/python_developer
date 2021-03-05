import statistics
import pandas as pd
import numpy as np
import xarray as xr
import re

#pip list
#pip freeze

data = [1, 3, 4, 5, 7, 9, 2] 
print(sum(data))
print(len(data))
print()
valor = sum(data) / len(data)
print(f"valor feito na mão: {valor}" )
x = statistics.mean(data) 
print("Mean is :", x) 

orden = pd.Index(data).sort_values()
print(orden) 

data_dois = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9],
             [np.nan, np.nan, np.nan]]
_df = pd.DataFrame(data_dois, columns = ['A', 'B', 'C'])
print(_df)

_df_new = _df.agg(['sum', 'min'])
print(_df_new)

_df_new_dois = _df.agg({'A' : ['sum', 'min'], 'B' : ['min', 'max']})
print(_df_new_dois)


#_df_new_tres = _df.agg(x=('A', max), y=('B', 'min'), z=('C', np.mean))
#print(_df_new_tres)

_df_new_quatro = _df.agg("mean", axis="columns")
print(_df_new_quatro)
