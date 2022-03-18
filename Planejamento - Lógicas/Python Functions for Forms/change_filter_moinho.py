def _fn(metadata):
    _list_datas =['Código Unidades', 'Equipamentos', 'Relatórios'] +  aux_ocultar_colunas_form + ['Total Dias', 'Total Horas']
    _columns = metadata['columns']
    for n in range(len(_columns)):
        if n >= 0:
            metadata['columns'][n]["header"] = index1[n-1]
            if n in (_list_datas):
                metadata['columns'][0]["hidden"] = True
                metadata['columns'][n]["hidden"] = True
            else:
                metadata['columns'][n]["hidden"] = False    
        
    return metadata

result = _fn