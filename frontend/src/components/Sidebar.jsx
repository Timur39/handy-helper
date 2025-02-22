import { Menu } from "antd";
import { Link } from "react-router-dom";
import { UserOutlined, ContainerOutlined, FormOutlined, HomeOutlined, YoutubeOutlined, DollarOutlined} from "@ant-design/icons";

const Sidebar = () => {
  const items = [
    {
      label: <Link to="/">Главная</Link>,
      key: "Sites",
      icon: <HomeOutlined />,
    },
    {
      label: <Link to="/News">Новости</Link>,
      key: "News",
      icon: <ContainerOutlined />,
    },
    {
      label: <Link to="/Plans">Планы</Link>,
      key: "Plans",
      icon: <FormOutlined />,
    },
    {
      label: <Link to="/Quotes">Котировки</Link>,
      key: "Quotes",
      icon: <DollarOutlined />,
    },
    {
      label: <Link to="/Video">Видео</Link>,
      key: "Video",
      icon: <YoutubeOutlined />,
    },
    {
      label: <Link to="/Achievement">Успеваемость</Link>,
      key: "Achievement",
      icon: <UserOutlined />,
    },
  ];

  return (
    <div className="w-48 min-w-48 h-screen fixed top-[70px] z-50">
      <Menu
        mode="inline"
        defaultSelectedKeys={["dashboard"]}
        items={items}
        theme="dark"
        className="bg-zinc-900 h-full"
    
      />
    
    </div>
  );
};

export default Sidebar;