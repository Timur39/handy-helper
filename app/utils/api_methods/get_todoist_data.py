from todoist_api_python.api_async import TodoistAPIAsync
from app.dependencies import todoist_api_token
from datetime import datetime


async def get_today_tasks():
    api = TodoistAPIAsync(todoist_api_token)
    result = []
    
    try:
        tasks = await api.get_tasks()
        for task in tasks:
            if task.due and task.due.date == datetime.now().strftime("%Y-%m-%d"):
                result.append({'title': task.content, 'link': task.url, 'priority': task.priority, 'description': task.description})
        return result
    except Exception as error:
        return f'Ошибка: {error}'
        

