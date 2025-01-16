import axiosInstance from './axiosInstance';


export const getGmailData = async () => {
  try {
    const response = await axiosInstance.get('/gmail/emails');
    return response.data;
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }
};

export const GmailFields = [
  { key: "title", label: "Название"},
  { key: "link", label: "Ссылка", isLink: true },
  { key: "date", label: "Дата" },
];

export default { getGmailData, GmailFields };
