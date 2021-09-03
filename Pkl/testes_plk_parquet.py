import pickle
import pandas as pd
file = pd.read_pickle('C:\\Users\\alexsandro.ignacio\\Downloads\\abertura_cd_1p.pkl')
print(f"\nQuantidades de Registros: {file.shape[0]}\n")
print(file.head(500))

file_dois = pd.read_parquet('C:\\Users\\alexsandro.ignacio\\Downloads\\468078d78e17478f9cf3d50f4e6d94bb.parquet')
print(f"\nQuantidades de Registros: {file_dois.shape[0]}\n")
print(file_dois.head(10))





