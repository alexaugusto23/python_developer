function(view, send){
    const $base = $(view.tagId)
    const $btnDownload = $base.find('.btnDownloadTable')
    
    $btnDownload.on("click", () => {
      //Execute button
      send('modelManager/previewNode/', {node: 'exportar_colaboracao_gcia_area'}, { type: 'POST' }, response => {
        console.log(response)
        
        //Download
        const downloadsFolder = `${__currentSession.modelInfo.uri.substring(0, __currentSession.modelInfo.uri.lastIndexOf("/")+1)}Export/`
        const fileName = "Ajuste Comercial-Gcia. Area.xls"
        const query = [`sources=${downloadsFolder}${fileName}`]
        query.push(`auth_token=${__currentToken}`)
        query.push(`session_key=${__currentSession.session_key}`)
        const url = `${__apiURL}/fileManager/download/?${query.join('&')}`
        
        const a = document.createElement('a')
        document.body.appendChild(a)
        a.style = 'display: none'
        a.href = url
        a.download = fileName
        a.click()
        window.URL.revokeObjectURL(url)
      })
    })
  }