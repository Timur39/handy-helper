import SitesDataCard from "../components/SitesDataCard"
import { getModrinthData, ModrinthFields } from "../api/modrinth_api"
import { getGithubData, GithubFields } from "../api/github_api";
import { useQuery } from "@tanstack/react-query";
import { getGmailData, GmailFields } from "../api/gmail_api";



const Sites = () => {
  let isLoading = false
  const interval = 120000

  // Получаем данные через useQuery
  const { data: modrinthData, isLoading: isLoadingModrinth, error: errorModrinth } = useQuery({
      queryKey: ["modrinth"], 
      queryFn: getModrinthData,
      refetchInterval: interval,
  });

  const { data: githubData, isLoading: isLoadingGitHub, error: errorGitHub } = useQuery({
    queryKey: ["github"],
    queryFn: getGithubData,
    refetchInterval: interval,
  });

  const { data: gmailData, isLoading: isLoadingGmail, error: errorGmail } = useQuery({
    queryKey: ["gmail"],
    queryFn: getGmailData,
    refetchInterval: interval,
  });

  if (isLoadingModrinth || isLoadingGitHub || isLoadingGmail) {
    isLoading = true
  }

  if (errorModrinth || errorGitHub || errorGmail) {
    return <div>Ошибка загрузки данных</div>;
  }

return <div className="flex gap-12">
    <SitesDataCard title={"Modrinth"} icon={"https://cdn.icon-icons.com/icons2/3913/PNG/72/modrinth_logo_icon_248441.png"} data={modrinthData} fields={ModrinthFields} isLoading={isLoading} />
    <SitesDataCard title={"GitHub"} icon={"https://cdn.icon-icons.com/icons2/936/PNG/72/github-logo_icon-icons.com_73546.png"} data={githubData} fields={GithubFields} isLoading={isLoading} />
    <SitesDataCard title={"Gmail"} icon={"https://cdn.icon-icons.com/icons2/2631/PNG/72/gmail_new_logo_icon_159149.png"} data={gmailData} fields={GmailFields} isLoading={isLoading} />
  </div>;

  };

export default Sites;