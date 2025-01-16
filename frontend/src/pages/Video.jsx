import SitesDataCard from "../components/SitesDataCard";


const testFields = [
  {key: "title", label: "Заголовок"},
  {key: "description", label: "Описание"},
  {key: "link", label: "Ссылка", isLink: true},
  {key: "date", label: "Дата"},
];

const testData = [{
    title: "Заголовок ОЧЕНЬ ВАЖНЫХ планов!",
    description: "Описание ОЧЕНЬ ВАЖНЫХ планов!",
    link: "https://google.com",
    date: "2023-01-01",
},
{
  title: "Заголовок ОЧЕНЬ ВАЖНЫХ планов!",
  description: "Описание ОЧЕНЬ ВАЖНЫХ планов!",
  link: "https://google.com",
  date: "2023-01-01",
},
{
  title: "Заголовок ОЧЕНЬ ВАЖНЫХ планов!",
  description: "Описание ОЧЕНЬ ВАЖНЫХ планов!",
  link: "https://google.com",
  date: "2023-01-01",
}]


const Video = () => {
    return <div>
    <SitesDataCard title={"Видео"} icon={"https://cdn.icon-icons.com/icons2/1860/PNG/72/videocamera2_118060.png"} data={testData} fields={testFields} />
    </div>;
  };
  
export default Video;