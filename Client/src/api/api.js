import axios from 'axios';

const instance = axios.create({
    baseURL: 'http://192.168.0.102:3000/api/',
    timeout: 5000,
    headers:{
        'Content-Type': 'application/json',
    },
})

export default instance;