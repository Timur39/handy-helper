import axiosInstance from './axiosInstance';


export const getYoutubeData = async () => {
  try {
    const response = await axiosInstance.get('/youtube_videos');
    return response.data;
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }
};

export const YoutubeFields = [
  { key: "title", label: "Название" },
  { key: "url", label: "Ссылка", isLink: true },
  { key: "preview_url", label: "Превью", isLink: true },
  { key: "duration", label: "Длительность" },
  { key: "date", label: "Дата" },
];

export default { getYoutubeData, YoutubeFields };
