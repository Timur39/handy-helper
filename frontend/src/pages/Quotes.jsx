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


const Quotes = () => {
    return <div>
    <SitesDataCard title={"Котирвки"} icon={"https://cdn.icon-icons.com/icons2/1526/PNG/72/dollarbills_106609.png "} data={testData} fields={testFields} />
    </div>;
  };
  
  export default Quotes;