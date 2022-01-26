import json 

# Nested list comprehension
matrix1 = [ f'{i, j}' for i in range(1,145) for j in range(1,7)]
  
print(matrix1)

# Nested list comprehension tuple 
matrix2 = [f'{i,j}'for i, j in zip(range(1, 145), range(1, 7))]

# Nested list example
_n = 1
_cols = ['{' + f'"type":"numeric","field":"Period_{i:03d}","style":' + '{' + '"color":"#000","backgroundColor":"#FFF8E3"'+ '}' + f',"format":"0,0","header":"S{j}","readOnly":false,"columnLength":"5"' + '}' for i in range(1, 145) for j in range(1, 7)]
print(_cols) 

# example de concatenation dates with weeks.
#_ind = (pd.date_range('2022',periods=36, freq='M')).astype(str).str[:7]
_ind = indice_temporal.to_list()
_ind = [i for i in _ind for _ in range(6)]

_df = pd.DataFrame({'mes':_ind})
_df['sem'] = 1
_df['sem'] = _df.groupby(['mes']).agg({'sem':'cumsum'}).astype(str)
_df['mes_sem'] = _df['mes']+' S'+_df['sem']

result = _df['mes_sem'].to_list()

# Nested columns receive new index.
_df = pd.DataFrame({'label':indice_temporal.to_list()})
_df['colspan'] = 6

result = _df.to_dict('record')


# with open('data.json', 'a', encoding='utf-8') as file: 
#     file.write(json.dump(data, file, ensure_ascii=False, indent=4).encode())
# file.close()
    




"""

"a"  - Escreve ao final do arquivo; se este não existir, é criado
"r"  - Abre o arquivo para a leitura, se não existir, lançar um eerro de IOError
"r+" - Abra um arquivo para leitura e escrita. Se não existe, lança um erro IOError
"w"  - Abre um arquivo para escrita. Se existe, ele 'trunca' tudo e escreve por cima. Se não existir o arquivo, ele cria
"w+" - Abre para leitura e escrita. Se existe, apaga todo conteúdo e escreve por cima. Se não existir o arquivo, ele cria
"ab", "rb", "r+b", "wb", "w+b" - Abre arquivos para trabalhar com entrada e saída no modo binário, para plataformas Windows e Macintosh
    
"""