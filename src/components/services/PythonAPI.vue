<script>
import ApiClient from '../utils/ApiClient'

export default {
  name: 'PythonAPI',
  runScript: function (params, callback, errorHandler) {
    let targetPath = '/api/python-shell'
    console.log(params)
    ApiClient.create(targetPath, params, (response) => {
      callback(response)
    }, (error) => {
      console.log(error)
      errorHandler(error)
    })
  }
}
</script>
