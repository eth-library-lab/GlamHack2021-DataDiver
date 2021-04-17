import axios from 'axios'

const apiClient = axios.create({
    // Vue sends requests from the user's browser so the api url must be publicly accessible, not just name spaced in docker-compose 
    baseURL: process.env.VUE_APP_API_BASE_URL, //load from env file
    withCredentials: false,
    headers: {
        'Content-Type': 'multipart/form-data'
    },
    timeout:10000,

})

export default {
    generatePreview(selectedFile) {
        let formData = new FormData()
        formData.append('zipfile', selectedFile)    
        let headers = { headers: {
                'Content-Type': 'multipart/form-data'
                }
            }
        return apiClient.post('preview', formData, headers)
    }
}