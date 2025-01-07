// import apiClient from "./apiClient";
import axios from 'axios';




const api = axios.create({
  baseURL: 'http://localhost:8000/api', // URL вашего бэкенда
});

export const getUsers = async () => {
  try {
    const response = await api.get('/users'); // Получаем список пользователей
    console.log(response.data);
    return response.data;
  } catch (error) {
    console.error('Ошибка при запросе данных:', error);
    return [];
  }
};