import axios from '../api/api.js';

class AuthService {

    login(user){
        return axios
                .post('auth/signin', {
                    email: user.email,
                    password: user.password,
                })
                .then(response => {
                    let user = JSON.stringify(response.data);
                    if(response.data.accessToken) {
                        localStorage.setItem('user', user);
                    }
                    return JSON.parse(user);
                })
    }

    logout() {
        localStorage.removeItem('user');
    }

    register(user){
        return axios.post('auth/signup', {
            username: user.username,
            name: user.name,
            classCode: user.classCode,
            studentCode: user.studentCode,
            bankBranch: user.bankBranch,
            bankNum: user.bankNum,
            OISPCode: user.OISPCode,
            role: user.role,
            email: user.email,
            password: user.password, 
        });
    }
}

export default new AuthService();