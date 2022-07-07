# example de concatenation dates with weeks.
#_ind = (pd.date_range('2022',periods=36, freq='M')).astype(str).str[:7]
_ind = indice_temporal.to_list()
_ind = [i for i in _ind for _ in range(6)]

_df = pd.DataFrame({'mes':_ind})
_df['sem'] = 1
_df['sem'] = _df.groupby(['mes']).agg({'sem':'cumsum'}).astype(str)
_df['mes_sem'] = _df['mes']+' S'+_df['sem']

_dims = ['Código Unidades', 'Equipamentos', 'Relatórios']
_list = _df['mes_sem'].to_list()

# [format_title(d, False) for d in _dims] + [format_title(l, True) for l in _list]


result = _dims + _list