def _fn(metadata):
  
    _columns = metadata['columns']
    for n in range(len(_columns)):
        if n >= 0:
            metadata['columns'][n]["header"] = indice_troca_de_datas_dias_calendario_soma1[n]
            if n in (aux_ocultar_colunas_form):
                metadata['columns'][0]["hidden"] = True
                metadata['columns'][n]["hidden"] = True
            else:
                metadata['columns'][n]["hidden"] = False    
        
    return metadata

result = _fn