import axiosInstance from './axiosInstance';


export const getGithubData = async () => {
  try {
    const response = await axiosInstance.get('/github_notifications');
    return response.data;
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }
};

export const GithubFields = [
  { key: "actor", label: "Автор"},
  { key: "type", label: "Тип действия" },
  { key: "description", label: "Описание"},
  { key: "repo", label: "Репозиторий"},
//   { key: "repo-url", label: "Ссылка", isLink: true },
  { key: "actor_url", label: "Ссылка на автора", isLink: true },
//   { key: "avatar", label: "Аватар", isImg: true },
  { key: "created_at", label: "Дата", IsData: true},
];

export default { getGithubData, GithubFields };
