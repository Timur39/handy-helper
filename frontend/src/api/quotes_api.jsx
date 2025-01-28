import axiosInstance from './axiosInstance';


export const getQuotesData = async () => {
  try {
    const response = await axiosInstance.get('/prices');
    return response.data;
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }
};

export const QuotesFields = [
  { key: "title", label: "Название" },
  { key: "price", label: "Цена", },
  { key: "ticker", label: "Тикер" },
];

export default { getQuotesData, QuotesFields };
