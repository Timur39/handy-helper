import SitesDataCard from "../components/SitesDataCard";
import { getNewsData, NewsFields } from "../api/news_api";
import { useQuery } from "@tanstack/react-query";

const News = () => {
    let isLoading = false
    const interval = 120000

    // Получаем данные через useQuery
    const { data: NewsData, isLoading: isLoadingNews, error: errorNews } = useQuery({
        queryKey: ["news"], 
        queryFn: getNewsData,
        refetchInterval: interval,
    });

    
    if (isLoadingNews) {
      isLoading = true
    }

    if (errorNews) {
      return <div>Ошибка загрузки данных</div>;
    }
    return <div>
    <SitesDataCard title={"Новости"} icon={"https://cdn.icon-icons.com/icons2/625/PNG/72/newspaper_icon-icons.com_57398.png"} data={NewsData} fields={NewsFields} isLoading={isLoading} />

    </div>;
  };
  

export default News;