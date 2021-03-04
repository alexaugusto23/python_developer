#Função: Set domain

def _fn(dataArray,domainDic, defaultValue=None):
    _da = dataArray
    for key in domainDic:
        _da = _da.reindex({key:domainDic[key].values})
        _da = _da.rename({key:domainDic[key].name})
    if not defaultValue is None:
        _da = _da.fillna(defaultValue)
    return _da

result = _fn

#Função: Build Report
def _fn(values,name="Report", report_index=None):
    _titles = [str(xx.name) for xx in values]
    _index = None
    if report_index is None:
        _index = pd.Index( _titles, name=name)
    else:
        _index = report_index
    
    return xr.concat(values,_index)

result = _fn

#Função: Create dataArray

def _fn(value,coords,dtype=None):
    _data = np.full( tuple([(len(x)) for x in coords]),value, dtype=dtype )
    return xr.DataArray( _data, coords )

result = _fn

#Função:Find
def _fn(param1, param2, compareType=1, caseSensitive = True):
    """
    param1: value or indexarray for compare
    param2: index compare to
    compareType: exact=1, start_with=2, end_with=3, contain=4  
    caseSensitive: able to differentiate between uppercase and lowercase (by default True)

    If param1 is a scalar (numeric or str) and param2 is an index:  return a dataArray indexed by param2 with True on ocurrences of param2
        Ex. result = find("te", region, cp.end_with)
    If param1 is an index and param2 is an index too:  return a dataArray indexed by param1 and param2 with True on ocurrences of param1 on param2
        Ex. result = find(subregion, region, cp.contain)

    """
    def _internalFn(item,value):
        if not isinstance(item,str):
            item = str(item)
        if not isinstance(value,str):
            value = str(value)
            
        if compareType==1:
            if caseSensitive:
                return item == value
            else:
                return item.lower() == value.lower()
        elif compareType==2:
            if caseSensitive:
                return item[:len(value)] == value
            else:
                return item[:len(value)].lower() == value.lower()                                    
        elif compareType==3:
            if caseSensitive:
                return item[-len(value):] == value
            else:
                return item[-len(value):].lower() == value.lower()                    
        elif compareType==4:
            if caseSensitive:
                return value in item
            else:
                return value.lower() in item.lower()

    if (isinstance(param1,str) or str(param1).isnumeric()) and isinstance(param2,pd.Index):
        vfn = np.vectorize(_internalFn)
        return xr.DataArray(vfn(param2.values,param1),[param2])

    if isinstance(param1,pd.Index) and isinstance(param2,pd.Index):
        _res = create_dataarray(False, [param1,param2], dtype=bool)
        for row in param1.values:
            for col in param2.values:
                _res.loc[ {param1.name:slice(row,row), param2.name:slice(col,col) }] = _internalFn(col,row)
        return _res 
            
result = _fn


#Função:
#Função:
#Função:
#Função:
#Função:
#Função:
#Função:
#Função:
#Função:
#Função:
#Função:
#Função:
