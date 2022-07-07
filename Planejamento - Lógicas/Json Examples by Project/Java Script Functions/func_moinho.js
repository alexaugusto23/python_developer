function (hotInstance, TD, row, col, prop, value, cellProperties) {
    const dataRow = hotInstance.getSourceDataAtRow(row);
    const rel = dataRow.relatorio;
    if (dataRow.id >= 0) {
        cellProperties.readOnly = false;
    }
    if (rel == 'Marchas') {
        TD.style.background = '#D8EBBF';
        TD.style.fontWeight = 'bold';
    }
    if (rel == 'Horarios de Ponta') {
        if (value == 0) {
            TD.style.background = '#EAFB15';
            TD.style.color = '#EAFB15';
        } else {
            TD.style.background = '#F3F3F3';
        }
    }
    if (rel == 'Manutenção Semanal') {
        TD.style.background = '#F3F3F3';
    }
    if (rel == 'Grandes Paradas') {
        TD.style.background = '#FFF8E3';
    }
    if (rel == 'Com ou Sem Contrato') {
        TD.style.background = '#FFF8E3C';
    }
    if (rel == 'Horas Manuntenção') {
        TD.style.background = '#FFF8E3';
    }
    if (rel == 'Outros') {
        TD.style.background = '#FFF8E3';
    }
    if (dataRow.id >= 0) {
        if (rel == 'Horarios de Ponta') {
            cellProperties.format = '0.0000'
        }
    }
}
