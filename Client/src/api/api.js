import axios from 'axios';

const instance = axios.create({
    baseURL: 'http://10.128.161.24:3000/api/',
    timeout: 5000,
    headers:{
        'Content-Type': 'application/json',
    },
})

export default instance;