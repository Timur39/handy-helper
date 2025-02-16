from todoist_api_python.api_async import TodoistAPIAsync
from app.dependencies import todoist_api_token
from app.schemas.api_schemas import Todoist_Schema
from datetime import datetime


async def get_today_tasks() -> list[Todoist_Schema]:
    api = TodoistAPIAsync(todoist_api_token)
    result = []
    
    try:
        tasks = await api.get_tasks()
        for task in tasks:
            if task.due and task.due.date == datetime.now().strftime("%Y-%m-%d"):
                result.append(Todoist_Schema(title=task.content, 
                                             link=task.url, 
                                             priority=task.priority, 
                                             description=task.description))
        return result
    except Exception as error:
        return f'Ошибка: {error}'
        

