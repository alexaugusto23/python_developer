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
}