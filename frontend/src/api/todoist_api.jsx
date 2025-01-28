import axiosInstance from './axiosInstance';


export const getTodoistData = async () => {
  try {
    const response = await axiosInstance.get('/todoist_tasks');
    return response.data;
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }
};

export const TodoistFields = [
  { key: "title", label: "Название" },
  { key: "link", label: "Ссылка", isLink: true },
  { key: "description", label: "Описание" },
  { key: "priority", label: "Приоритет" },
];

export default { getTodoistData, TodoistFields };
