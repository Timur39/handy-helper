import axiosInstance from './axiosInstance';


export const getNewsData = async () => {
  try {
    const response = await axiosInstance.get('/news/news');
    return response.data;
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }
};

export const NewsFields = [
  { key: "text", label: "Название" },
  { key: "link", label: "Ссылка", isLink: true },
  { key: "date", label: "Дата" },
  { key: "channel", label: "Источник" },
];

export default { getNewsData, NewsFields };
