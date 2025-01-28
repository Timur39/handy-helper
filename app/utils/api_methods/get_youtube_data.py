import datetime
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import os


SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]

def get_creds_auth(creds):
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file('app/credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        
    # Сохраняем токен для будущих запусков
    with open('app/token_youtube.json', 'w') as token:
        token.write(creds.to_json())

    return creds
def get_youtube_creds():
    creds = None

    # Проверка существующего токена
    if os.path.exists('app/token_youtube.json'):
        creds = Credentials.from_authorized_user_file('app/token_youtube.json', SCOPES)

    # Если токен отсутствует или недействителен, выполняем авторизацию
    if not creds or not creds.valid:
        creds = get_creds_auth(creds)

    return build("youtube", "v3", credentials=creds)

def get_subscriptions():
    """
    Получает список каналов, на которые вы подписаны.
    """
    youtube = get_youtube_creds()

    subscriptions = []
    request = youtube.subscriptions().list(
        part="snippet",
        mine=True,  # Получение подписок для текущего пользователя
        maxResults=80,  # Ограничиваем количество результатов
    )
    response = request.execute()

    for item in response.get("items", []):
        channel_title = item["snippet"]["title"]
        subscriptions.append(channel_title)

    return subscriptions


def get_youtube_videos(channel_names=get_subscriptions()):
    # Создаём клиент YouTube API
    """
    Получает список последних видео с каналов, на которые вы подписаны.
    
    :param channel_names: список имен каналов
    :param max_results: ограничение на количество результатов (по умолчанию 5)
    :return: список видео, каждый элемент которого - словарь с полями title, url, preview_url, date
    """
    youtube = get_youtube_creds()

    videos = []

    for username in channel_names:
        # Получаем ID канала по username
        channel_request = youtube.search().list(
            part="id, snippet",
            q=username,
            type="channel",
        )
        channel_response = channel_request.execute()

        # Точное сравнение с учетом регистра
        channel = next(item for item in channel_response['items'] if item["snippet"]["title"] == username), None
        
        channel_id = channel[0]["id"]['channelId']
        
        # # Получение загрузочного плейлиста канала (uploads playlist)
        # channel_uploads = youtube.channels().list(
        #     part="contentDetails",
        #     id=channel_id
        # ).execute()
        
        # uploads_playlist_id = channel_uploads["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

        today = datetime.datetime.now().date()
        
        # Получение последних видео из загрузочного плейлиста
        playlist_response = youtube.search().list(
            part="snippet",
            channelId=channel_id,
            order="date",  # Сортировка по дате публикации
            publishedAfter=f"{today}T00:00:00Z",  # Сегодняшний день в формате ISO
            type="video",  # Только видео
            maxResults=5  # Ограничение на количество результатов
        )
        playlist_response = playlist_response.execute()

        for item in playlist_response["items"]:
            video_date = item["snippet"]["publishedAt"]
            video_title = item["snippet"]["title"]
            video_id = item["id"]["videoId"]
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            video_preview_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"

            # Получаем длительность видео
            video_duration_request = youtube.videos().list(
                part="contentDetails",
                id=item['id']['videoId']
            ).execute()

            video_duration = video_duration_request["items"][0]["contentDetails"]["duration"]


            # Проверка на длительность видео (исключаем шортсы)
            if "M" in video_duration or "H" in video_duration:  # Проверяем, что есть минуты или часы
                videos.append({"title": video_title, 
                               'duration': video_duration,
                               "url": video_url, 
                               'preview_url': video_preview_url, 
                               'date': video_date})
        
    return videos

# Получение последних видео
my_subscriptions = get_subscriptions()

latest_videos = get_youtube_videos(my_subscriptions)


for video in latest_videos:
    print(f"Название: {video['title']}, Ссылка: {video['url']} Превью: {video['preview_url']}")
