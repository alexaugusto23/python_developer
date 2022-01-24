import json 

data = '{"type": "numeric", "field": null, "style": {"color": "#000", "backgroundColor": "#FFF8E3"},"format": "0.00", "header": null , "readOnly": "false", "columnLength": "10"}'

print (json.loads(data))

data = json.loads(data)

_n1 = 144
_n2 = 6

new_data = []

for i in range (1, _n1 + 1):
    data["field"] = f'Period_{i:03d}'
    # with open('data.json', 'a', encoding='utf-8') as file: 
    #     file.write(json.dump(data, file, ensure_ascii=False, indent=4).encode())
    # file.close()
    
    print(data)

    # for s in range (1,_n2 + 1):
        
    #     object_json['header'] = f'Sem_{s:02d}'
    #     print(object_json)

"""

"a"  - Escreve ao final do arquivo; se este não existir, é criado
"r"  - Abre o arquivo para a leitura, se não existir, lançar um eerro de IOError
"r+" - Abra um arquivo para leitura e escrita. Se não existe, lança um erro IOError
"w"  - Abre um arquivo para escrita. Se existe, ele 'trunca' tudo e escreve por cima. Se não existir o arquivo, ele cria
"w+" - Abre para leitura e escrita. Se existe, apaga todo conteúdo e escreve por cima. Se não existir o arquivo, ele cria
"ab", "rb", "r+b", "wb", "w+b" - Abre arquivos para trabalhar com entrada e saída no modo binário, para plataformas Windows e Macintosh
    
"""