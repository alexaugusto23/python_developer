function (view, send){
    const $base = $(view.tagId)
    const $btnUpload = $base.find('button.btnUploadTemplate')
    const $btnDownload = $base.find('button.btnDownloadTemplate')
    const $btnDownloadBase = $base.find('button.btnDownloadBaseTemplate')
    const $btnClearMessage = $base.find('button.btnClearMessage')
    const $uploader = $base.find('#TemplateUploader')
    const $uploadStatus = $base.find('#TemplateUploadStatus')
    const folderPath = `${__currentSession.modelInfo.uri.substring(0, __currentSession.modelInfo.uri.lastIndexOf("/")+1)}Inputs/`
    const baseFolderPath = `${__currentSession.company_code}/Public/.BaseModel/Inputs/`
    let filename = ''
    
    // button listeners
    $btnUpload.on('click', e => {
      filename = $(e.target).closest('tr').find('td:first-child')[0].innerText
      $uploader.click()
    })
    
    $btnDownload.on('click', e => {
      filename = $(e.target).closest('tr').find('td:first-child')[0].innerText
      
      const query = [`sources=${folderPath}${filename}`]
      query.push(`auth_token=${__currentToken}`)
      query.push(`session_key=${__currentSession.session_key}`)
      const url = `${__apiURL}/fileManager/download/?${query.join('&')}`
      const a = document.createElement('a')
      document.body.appendChild(a)
      a.style = 'display: none'
      a.href = url
      a.download = filename
      a.click()
      window.URL.revokeObjectURL(url)
    })
    
    $btnDownloadBase.on('click', e => {
      filename = $(e.target).closest('tr').find('td:first-child')[0].innerText
      
      const query = [`sources=${baseFolderPath}${filename}`]
      query.push(`auth_token=${__currentToken}`)
      query.push(`session_key=${__currentSession.session_key}`)
      const url = `${__apiURL}/fileManager/download/?${query.join('&')}`
      const a = document.createElement('a')
      document.body.appendChild(a)
      a.style = 'display: none'
      a.href = url
      a.download = filename
      a.click()
      window.URL.revokeObjectURL(url)
    })
    
    $btnClearMessage.hide()
    $btnClearMessage.on('click', e => {
      $uploadStatus.html('')
      $btnClearMessage.hide()
    })
    
    //uploader
    $uploader.on('click', e => {
      e.currentTarget.value = ''
    })
    $uploader.on('change', e => {
      $uploadStatus.html('')
      const files = e.currentTarget.files
      const url = `${__apiURL}/fileManager/upload/`
      
      if(files[0].name === filename){
        const xhr = new XMLHttpRequest()
        const fd = new FormData()
        xhr.open('POST', url, true)
        xhr.setRequestHeader('Authorization', `Token ${__currentToken}`)
        xhr.setRequestHeader('session-key', __currentSession.session_key)
        xhr.onreadystatechange = e => {
            if (xhr.readyState === 4 && xhr.status === 200) {
              $uploadStatus.html(`<div style='color: white;'><b>The file ${filename} has been successfully uploaded</b></div>`)
            } else if (xhr.readyState === 4 && xhr.status !== 200) {
              $uploadStatus.html(`<div style="color: red;"><b>${e.currentTarget.status} - ${e.currentTarget.statusText}</b></div>`)
            }
            $btnClearMessage.show()
            $btnUpload.prop('disabled',false)
        }
        
        xhr.upload.addEventListener("progress", e => {
          if (e.lengthComputable) {
            const percentage = Math.round((e.loaded * 100) / e.total)
            console.log(percentage)
            $uploadStatus.html(`<div class="progress progress-striped active" style="width:100%;">
              <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="${percentage}" aria-valuemin="0" aria-valuemax="100" style="width:${percentage}%;">
                ${percentage}%
              </div>
            </div>`)
          }
        })
        
        xhr.upload.addEventListener('error', e => {
          console.log(e)
        })
       
        fd.append('action','uploadFileToModelFolder')
        fd.append('folder_path', folderPath)
        fd.append('chunk', 0)
        fd.append('chunks', 1)
        fd.append('files',files[0])
        fd.append('name',filename)
        xhr.send(fd)
        
        $btnUpload.prop('disabled',true)
      } else {
        $uploadStatus.html(`<div style="color: red;"><b>You can only upload a file named ${filename}</b></div>`)
        $btnClearMessage.show()
      }
    })
    
    
    
  }