import axiosInstance from './axiosInstance';


export const getStepikData = async () => {
  try {
    const response = await axiosInstance.get('/stepik_user_activity');
    return response.data;
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }
};

export const StepikFields = [
  { key: "id", label: "Название" },
  { key: "knowledge", label: "Знания", },
  { key: "solved_steps_count", label: "Задач пройдено" },
  { key: "issued_certificates_count", label: "Кол-во сертификатов" },
];

export default { getStepikData, StepikFields };
