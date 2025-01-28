import SitesDataCard from "../components/SitesDataCard";
import { getStepikData, StepikFields } from "../api/stepik_api";
import { useQuery } from "@tanstack/react-query";


const Achievement = () => {
  let isLoading = false
  const interval = 120000

  // Получаем данные через useQuery
  const { data: StepikData, isLoading: isLoadingStepik, error: errorStepik } = useQuery({
      queryKey: ["achievement"], 
      queryFn: getStepikData,
      refetchInterval: interval,
  });

  
  if (isLoadingStepik) {
    isLoading = true
  }

  if (errorStepik) {
    return <div>Ошибка загрузки данных</div>;
  }

  return <div>
    <SitesDataCard title={"Успеваемость"} icon={"/static/achievement_icon.png"} data={StepikData} fields={StepikFields} isLoading={isLoading} />
    </div>;
  };
  
export default Achievement;