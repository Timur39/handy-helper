import SitesDataCard from "../components/SitesDataCard";
import { useQuery } from "@tanstack/react-query";
import { getTodoistData, TodoistFields} from "../api/todoist_api"

const Plans = () => {
  let isLoading = false
  const interval = 120000

  // Получаем данные через useQuery
  const { data: TodoistData, isLoading: isLoadingTodoist, error: errorTodoist } = useQuery({
      queryKey: ["todoist"], 
      queryFn: getTodoistData,
      refetchInterval: interval,
  });

  
  if (isLoadingTodoist) {
    isLoading = true
  }

  if (errorTodoist) {
    return <div>Ошибка загрузки данных</div>;
  }
    return <div>
    <SitesDataCard title={"Планы"} icon={"/static/plan_icon.png"} data={TodoistData} fields={TodoistFields} />
    </div>;
  };
  
  export default Plans;