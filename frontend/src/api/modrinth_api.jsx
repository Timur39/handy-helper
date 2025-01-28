import axiosInstance from './axiosInstance';


export const getModrinthData = async () => {
  try {
    const response = await axiosInstance.get('/modrinth_notifications');
    return response.data;
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }
};

export const ModrinthFields = [
  { key: "title", label: "Название"},
  { key: "description", label: "Описание" },
  { key: "game_versions", label: "Версии", isList: true },
  { key: "link", label: "Ссылка", isLink: true },
  { key: "loaders", label: "Загрузчики", isList: true },
  { key: "updated", label: "Дата" },
];

export default { getModrinthData, ModrinthFields };
