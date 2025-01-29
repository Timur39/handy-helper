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
  { key: "preview_url", label: "Превью", isImg: true},
  { key: "title", label: "Название" },
  { key: "duration", label: "Длительность" },
  { key: "views", label: "Просмотры" },
  { key: "date", label: "Дата" },
  { key: "url", label: "Ссылка", isLink: true },
  { key: "channel", label: "Канал" },
];

export default { getYoutubeData, YoutubeFields };
