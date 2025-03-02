import axios from 'axios';

const api = axios.create({
    baseURL: 'http://127.0.0.1:8000/',
    withCredentials: true
})

api.interceptors.request.use(
    (config) =>{
        const token = localStorage.getItem('access_token');
        if (token) {
            config.headers['Authorization'] = `Bearer ${token}`
        }
        return config;
    },
    (error) =>{
        return Promise.reject(error);
    }
)

api.interceptors.response.use(
    response => {
        return response;
    },
    async (error) => {
        console.log("Error de token"+ error)
        if (error.response.status === 401) {
            localStorage.setItem('session_expired', 'true');
            localStorage.removeItem('access_token');
            window.location.href = '/login';
            return Promise.reject(error);
        }
        return Promise.reject(error);
    }
)

export default api;