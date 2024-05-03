import axios from '../api/api.js';
import authHeader from './auth-header';

class UserService {
  getPublicContent() {
    return axios.get('test/all');
  }

  getStudentBoard() {
    return axios.get('test/student', { headers: authHeader() });
  }

  getOispBoard() {
    return axios.get('test/oisp', { headers: authHeader() });
  }
}

export default new UserService();