import axios from 'axios';

const axiosInstance = axios.create({
  baseURL: 'http://localhost:8000', // Замените на ваш URL
  headers: {
    'Content-Type': 'application/json',
  },
});

export default axiosInstance;