//"customCellFunction": "function(hotInstance, TD, row, col, prop, value, cellProperties){ const dataRow = hotInstance.getSourceDataAtRow(row); if (dataRow.id_col==-1){TD.style.color = '#000';TD.style.background = '#adadad';cellProperties.readOnly = false;}}"


// Permite editar a linha do form quando a informação veem do model dataframe.
let func = function(hotInstance, TD, row, col, prop, value, cellProperties)
{ 
    const dataRow = hotInstance.getSourceDataAtRow(row); 
    if (dataRow.id_key == 0)
        {TD.style.color = '#000';
        TD.style.background = '#F3F3F3';
        cellProperties.readOnly = false;
    }
}


function funcB(hotInstance, TD, row, col, prop, value, cellProperties) 
{   const dataRow = hotInstance.getSourceDataAtRow(row); 
    const rel = dataRow.relatorio; 
    if (dataRow.id >= 0) { 
        cellProperties.readOnly = false; 
    } 
    if (rel == 'Marchas') { 
        TD.style.background = '#F3F3F3'; TD.style.fontWeight = 'bold'; 
    } 
    if (rel == 'Horarios de Ponta') { 
        TD.style.background = '#F3F3F3'; 
    } 
    if (rel == 'Manutenção Semanal') { 
        TD.style.background = '#F3F3F3'; 
    } 
    if (rel == 'Grandes Paradas') { 
        TD.style.background = '#FFF8E3'; 
    } 
    if (rel == 'Dias Uteis') { 
        TD.style.background = '#FFF8E3C'; 
    } 
    if (rel == 'Horas Manuntenção') { 
        TD.style.background = '#FFF8E3'; 
    } 
    if (rel == 'Outros') { 
        TD.style.background = '#FFF8E3'; 
    } 
}


