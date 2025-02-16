import requests
from app.dependencies import user_id, client_id, client_secret
from app.schemas.api_schemas import Stepik_Schema

async def get_access_token():
    token_url = 'https://stepik.org/oauth2/token/'
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
    }

    response = requests.post(token_url, data=data)

    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'Failed to obtain access token', 'Error': {response.status_code}, 'Response': {response.text}}


async def get_user_activity() -> list[Stepik_Schema]:
    access_token = await get_access_token()
    url = f'https://stepik.org/api/users/{user_id}'

    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    user = []
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        user_data = response.json()['users'][0]
        user.append(
            Stepik_Schema(id=user_data['id'],
                          knowledge=user_data['knowledge'],
                          solved_steps_count=user_data['solved_steps_count'],
                          issued_certificates_count=user_data['issued_certificates_count'],
                          link=f'https://stepik.org/users/{user_data["id"]}/profile'))


        return user
    else:
        return f"Ошибка: {response.status_code}"
