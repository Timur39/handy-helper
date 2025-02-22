import requests
from datetime import datetime, timedelta
from app.dependencies import github_api_token
from app.schemas.api_schemas import Github_Schema

# Заголовки с авторизацией
headers = {
    "Authorization": f"Bearer {github_api_token}",
    "Content-Type": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}

async def get_github_notifications(timedelta_days=2) -> list[Github_Schema] | None:
    try:
        # Отправляем запрос к API
        response = requests.get('https://api.github.com/user/following', headers=headers)
        result = []
        # Проверяем статус ответа
        if response.status_code == 200:
            users = response.json()

            for user in users:
                responce_project = requests.get(f"https://api.github.com/users/{user['login']}/events", headers=headers)
                
                if responce_project.status_code == 200:
                    need_events = ["ReleaseEvent", "PushEvent", "CreateEvent", "WatchEvent"]
                    
                    event_data = responce_project.json()
                    event_data = [event for event in event_data if event["type"] in need_events]
    
                    if event_data:
                        for data in event_data:

                            # TODO: Не та тайм зона нужно переделать на utc +3
                            time_difference = datetime.now() - datetime.strptime(data['created_at'], '%Y-%m-%dT%H:%M:%SZ')
                            if time_difference > timedelta(days=timedelta_days):
                                continue

                            description = ''
                            
                            match data['type']:
                                case 'ReleaseEvent':
                                    description = data['payload']['release']['html_url']
                                case 'PushEvent':
                                    description = data['payload']['commits'][0]['message']
                                case 'CreateEvent':
                                    description = data['payload']['description']
                                case 'WatchEvent':
                                    description = data['payload']['action']

                            date_obj = datetime.astimezone().strptime(data['created_at'], "%Y-%m-%dT%H:%M:%SZ")
                            formatted_date = date_obj.strftime("%Y-%m-%d %H:%M")
                            result.append(
                                Github_Schema(
                                    actor=user['login'],
                                    type=data['type'],
                                    description=description,
                                    repo=data['repo']['name'],
                                    actor_url=user['html_url'],
                                    created_at=formatted_date,
                                ))
            return result
        
        else:
            return f"Ошибка: {response.status_code}, {response.text}"
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return