const Header = () => {
    return (
      <header className="bg-zinc-900 text-white p-2 shadow fixed top-0 left-0 right-0 z-50 flex items-center justify-between">
        <h1 className="text-xl font-bold">Удобный помощник</h1>
        <button className="bg-blue-500 hover:bg-blue-400 text-white font-bold py-2 px-6 rounded-[10px] md:ml-auto md:mr-4">Настройки</button>
        <button className="bg-blue-500 hover:bg-blue-400 text-white font-bold py-2 px-6 rounded-[10px]">Профиль</button>
      </header>
    );
  };
  export default Header;
