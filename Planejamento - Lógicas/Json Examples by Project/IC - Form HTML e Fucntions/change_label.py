def _fn(metadata):
    _list_datas =['idx_maquina_tipo', 'Código Unidades', 'Equipamentos', 'Relatórios'] +  aux_ocultar_colunas_form_moinhos_fornos + ['Total Dias', 'Total Horas']
    _columns = metadata['columns']
    for n in range(len(_columns)):
        if n >= 0:
            metadata['columns'][n]["header"] = format_title(index1[n-1], index1[n-1] in indice_troca_de_datas_dias_calendario.to_list())
            if n in (_list_datas):
                metadata['columns'][0]["hidden"] = True
                metadata['columns'][n]["hidden"] = True
            else:
                metadata['columns'][0]["hidden"] = True
                metadata['columns'][n]["hidden"] = False    
        
    return metadata

result = _fn