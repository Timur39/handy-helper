import requests
from datetime import datetime
from app.dependencies import modrinth_api_token, modrinth_user

# URL для получения уведомлений
BASE_URL = "https://api.modrinth.com/v2"
NOTIFICATIONS_ENDPOINT = f"{BASE_URL}/user/{modrinth_user}/notifications"

# Заголовки с авторизацией
headers = {
    "Authorization": f"Bearer {modrinth_api_token}",
    "Content-Type": "application/json",
}

async def get_modrinth_notifications(count=5):
    try:
        # Отправляем запрос к API
        response = requests.get(NOTIFICATIONS_ENDPOINT, headers=headers)
        result = []
        # Проверяем статус ответа
        if response.status_code == 200:
            notifications = response.json()

            for notification in notifications[0:count]:

                responce_project = requests.get(f"{BASE_URL}/project/{notification['body']["project_id"]}", headers=headers)
                
                if responce_project.status_code == 200:
                    data = responce_project.json()
                    # TODO: Не та тайм зона нужно переделать на utc +3
                    date_obj = datetime.strptime(data['updated'], "%Y-%m-%dT%H:%M:%S.%fZ")
                    formatted_date = date_obj.strftime("%Y-%m-%d %H:%M")

                    result.append({
                        'title': data['title'],
                        'game_versions': data['game_versions'][-1:-11:-1],
                        'updated': formatted_date,
                        'loaders': data['loaders'],
                        'description': data['description'],
                        'link': f'https://modrinth.com{notification['link']}'
                    })

                else:
                    return f"Ошибка: {responce_project.status_code}, {responce_project.text}"
        else:
            return f"Ошибка: {response.status_code}, {response.text}"
        
        return result
        
    except Exception as e:
        return f"Произошла ошибка: {e}"
