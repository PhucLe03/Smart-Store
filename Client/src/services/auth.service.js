import axios from '../api/api.js';

class AuthService {

    login(user) {
        return axios
            .post('auth/signin', {
                email: user.email,
                password: user.password,
            }, {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            })
            .then(response => {
                let user = JSON.stringify(response.data);
                if (response.data.accessToken) {
                    localStorage.setItem('user', user);
                }
                return JSON.parse(user);
            })
    }

    logout() {
        localStorage.removeItem('user');
    }

    register(user) {
        const formData = new FormData()
        const userdata = {
            username: user.username,
            name: user.name,
            // classCode: user.classCode,
            // studentCode: user.studentCode,
            // bankBranch: user.bankBranch,
            // bankNum: user.bankNum,
            // OISPCode: user.OISPCode,
            // role: user.role,
            email: user.email,
            password: user.password,
        }
        formData.append('user_register', JSON.stringify(userdata))
        formData.append('file', user.file_upload)
        return axios.post('auth/signup', formData,
            {
                headers:
                {
                    'Content-Type': 'multipart/form-data'
                    // 'Content-Type': 'application/x-www-form-urlencoded'
                }
            });
    }
}

export default new AuthService();