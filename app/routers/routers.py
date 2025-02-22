from fastapi import APIRouter, BackgroundTasks
from async_lru import alru_cache
from email.message import EmailMessage
from app.dependencies import SMTP_USER, SMTP_PASSWORD
import smtplib
from datetime import datetime

router = APIRouter(tags=["other"], prefix='')
ttl_cache = 60


def write_email(user_email: str) -> None:
    SMTP_HOST = "smtp.gmail.com"
    SMTP_PORT = 465

    email = EmailMessage()
    email['Subject'] = 'Удобный помощник'
    email['From'] = SMTP_USER
    email['To'] = user_email

    email.set_content(
        f'''
        <h1>Отчет за месяц ({datetime.now().strftime('%d.%m.%Y')})</h1>
        <h4>Пройдено заданий на степике: </h4>
        <h4>Пройдено задач в Todoist: </h4>
        <h4>Ударный режим Duolingo: </h4>
        <h4>Дней работы на GitHub: </h4>
        ''',
        subtype='html'
    )

    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(email)



@router.post('/send_email/{email}', summary="Отправить сообщение на email")
@alru_cache(ttl=ttl_cache)
async def send_email(email: str, bg_tasks: BackgroundTasks) -> dict[str, str] | None:
    try:
        bg_tasks.add_task(write_email, email)
        return {'status': 'Email was successfully sent'}

    except Exception as e:
        return {'error': str(e)}

