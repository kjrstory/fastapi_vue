import axios from 'axios'

const fastapi = (operation, url, params, success_callback, failure_callback) => {

    let method = operation 
    let content_type = 'application/json' 
    let body = JSON.stringify(params)

    let _url = process.env.VUE_APP_SERVER_URL + url
    if(method === 'get') {
        _url += "?" + new URLSearchParams(params)
    }

    let options = {
      method: method,
      headers: {
         "Content-Type": content_type
      }
    }

    if (method !== 'get') {
       options['data'] = body
    }

    axios(_url, options)
      .then(response => {
         if (response.status >= 200 && response.status < 300) {
            if (success_callback) {
                success_callback(response.data)
            }
         } else {
            response.json()
                .then(json => {
                    if (failure_callback) {
                        failure_callback(json)
                    } else {
                        alert(JSON.stringify(json))
                    }
                })
                .catch(error => {
                    alert(JSON.stringify(error))
                })
        }
       })
      .catch(error => {
        if (failure_callback) {
            failure_callback(error)
        }
      })
}

export default fastapi
