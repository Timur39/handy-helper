import React, { useEffect, useState } from 'react';
import { getUsers } from './api/userApi.js';

function App() {
  const [users, setUsers] = useState([]); // Состояние для данных
  const [loading, setLoading] = useState(true); // Состояние загрузки

  useEffect(() => {
    // Функция для загрузки данных
    const fetchData = async () => {
      const data = await getUsers();
      setUsers(data); // Сохраняем данные в состояние
      setLoading(false); // Устанавливаем флаг загрузки
    };

    fetchData(); // Вызываем функцию загрузки
  }, []); // [] означает, что useEffect выполнится один раз при загрузке

  
  if (loading) {
    return <p>Загрузка данных...</p>;
  }

  if (users.length === 0) {
    return <p>Нет данных для отображения</p>;
  }

  return (
    <div>
      <h1>Список пользователей</h1>
      <ul style={{ listStyleType: 'none', padding: 0 }}>
  {users.map((user) => (
    <li
      key={user.id}
      style={{
        padding: '10px',
        margin: '5px 0',
        border: '1px solid #ddd',
        borderRadius: '5px',
      }}
    >
      <strong>{user.username}</strong> <br />
      <span>{user.email}</span>
    </li>
  ))}
</ul>
    </div>
  );
}

export default App;


