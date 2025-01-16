from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from datetime import datetime
import os


# Скоупы для Gmail API
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


async def get_creds(creds):
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file('app/credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Сохраняем токен для будущих запусков
    with open('app/token.json', 'w') as token:
        token.write(creds.to_json())

    return creds


async def get_gmails(count=10):
    creds = None
    # Проверка существующего токена
    if os.path.exists('app/token.json'):
        creds = Credentials.from_authorized_user_file('app/token.json', SCOPES)
    # Если токен отсутствует или недействителен, выполняем авторизацию
    if not creds or not creds.valid:
        creds = await get_creds(creds)
    # Создаем сервис Gmail API
    service = build('gmail', 'v1', credentials=creds)

    # Получаем список сообщений
    results = service.users().messages().list(userId='me', maxResults=count).execute()
    messages = results.get('messages', [])

    if not messages:
        return 'Нет сообщений.'
    
    result = []
    for msg in messages:

        msg_id = msg['id']
        message = service.users().messages().get(userId='me', id=msg_id).execute()
        headers = message['payload'].get('headers', [])
        mail_title = next((header['value'] for header in headers if header['name'] == 'Subject'), 'Без темы')
        mail_date = next((header['value'] for header in headers if header['name'] == 'Date'), 'Без темы')
        # TODO: Не та тайм зона нужно переделать на utc +3
        date_obj = datetime.strptime(mail_date.split('(')[0].strip(), "%a, %d %b %Y %H:%M:%S %z")
        formatted_date = date_obj.strftime("%Y-%m-%d %H:%M")    
        # Формируем ссылку на сообщение
        message_link = f"https://mail.google.com/mail/u/0/#all/{msg_id}"
        result.append({'title': mail_title, 'date': formatted_date, 'link': message_link})
    
    return result
