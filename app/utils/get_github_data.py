import requests
from datetime import datetime, timedelta

API_TOKEN = "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"

# Заголовки с авторизацией
headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}
async def get_notifications(timedelta_days=2):
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
                    event_data = responce_project.json()
                    event_data = [event for event in event_data if event["type"] == "ReleaseEvent" or event["type"] == "PushEvent" or event["type"] == "CreateEvent" or event["type"] == "WatchEvent"]
    
                    if event_data:
                        for data in event_data:
                            # TODO: Не та тайм зона нужно переделать на utc +3
                            time_difference = datetime.now() - datetime.strptime(data['created_at'], '%Y-%m-%dT%H:%M:%SZ')
                            if time_difference > timedelta(days=timedelta_days):
                                continue

                            description = ''
                            if data['type'] == 'ReleaseEvent':
                                description = data['payload']['release']['html_url']
                            elif data['type'] == 'PushEvent':
                                description = data['payload']['commits'][0]['message']
                            elif data['type'] == 'CreateEvent':
                                description = data['payload']['description']
                            elif data['type'] == 'WatchEvent':
                                description = data['payload']['action']

                            date_obj = datetime.strptime(data['created_at'], "%Y-%m-%dT%H:%M:%SZ")
                            formatted_date = date_obj.strftime("%Y-%m-%d %H:%M")

                            result.append({
                                'actor': data['actor']['display_login'],
                                'type': data['type'],
                                'description': description,
                                'repo': data['repo']['name'],
                                # 'repo-url': data['repo']['url'],
                                'actor_url': user['html_url'],
                                # 'avatar': data['actor']['avatar_url'],
                                'created_at': formatted_date,
                                
                            })
                else:
                    print(f"Ошибка: {responce_project.status_code}, {responce_project.text}")
        else:
            print(f"Ошибка: {response.status_code}, {response.text}")
        
        return result
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")