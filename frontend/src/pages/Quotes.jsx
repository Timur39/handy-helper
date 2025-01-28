import SitesDataCard from "../components/SitesDataCard";
import { getQuotesData, QuotesFields } from "../api/quotes_api";
import { useQuery } from "@tanstack/react-query";


const Quotes = () => {
  let isLoading = false
  const interval = 120000

  // Получаем данные через useQuery
  const { data: quotesData, isLoading: isLoadingQuotes, error: errorQuotes } = useQuery({
      queryKey: ["quotes"], 
      queryFn: getQuotesData,
      refetchInterval: interval,
  });


  if (isLoadingQuotes) {
    isLoading = true
  }

  if (errorQuotes) {
    return <div>Ошибка загрузки данных</div>;
  }

return <div className="flex gap-12">
    <SitesDataCard title={"Котирвки"} icon={"/static/quotes_icon.png"} data={quotesData} fields={QuotesFields} isLoading={isLoading} />
  </div>;

  };

export default Quotes;