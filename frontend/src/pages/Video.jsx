import SitesDataCard from "../components/SitesDataCard";
import { getYoutubeData, YoutubeFields } from "../api/youtube_api";
import { useQuery } from "@tanstack/react-query";


const Video = () => {
  let isLoading = false
  const interval = 120000

  // Получаем данные через useQuery
  const { data: youtubeData, isLoading: isLoadingYoutube, error: errorYoutube } = useQuery({
      queryKey: ["youtube"], 
      queryFn: getYoutubeData,
      refetchInterval: interval,
  });


  if (isLoadingYoutube) {
    isLoading = true
  }

  if (errorYoutube) {
    return <div>Ошибка загрузки данных</div>;
  }

return <div className="flex gap-12">
    <SitesDataCard title={"Видео"} icon={"/static/video_icon.png"} data={youtubeData} fields={YoutubeFields} isLoading={isLoading} />
  </div>;

  };

export default Video;