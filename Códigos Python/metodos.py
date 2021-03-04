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

data_dois = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]