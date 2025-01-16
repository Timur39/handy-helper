from datetime import datetime, timedelta
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")

# Список каналов
CHANNELS = ['@Minecraftoday', '@naebnet']
MESSAGES_LIMIT = 20

async def get_news(timedelta_days=2):
    async with TelegramClient('news', API_ID, API_HASH) as client:
        all_posts = []

        for channel in CHANNELS:
            try:
                entity = await client.get_entity(channel)
                history = await client(GetHistoryRequest(
                    peer=entity,
                    offset_id=0,
                    offset_date=None,
                    add_offset=0,
                    limit=MESSAGES_LIMIT,
                    max_id=0,
                    min_id=0,
                    hash=0
                ))

                for message in history.messages:
                    post_date = message.date.strftime("%Y-%m-%d %H:%M")
                    post = {
                        "text": message.message, 
                        "link": f"https://t.me/{channel[1:]}/{message.id}",
                        "date": post_date,
                        "channel": channel
                    }
                    # TODO: Не та тайм зона нужно переделать на utc +3
                    time_difference = datetime.now() - datetime.strptime(post_date, "%Y-%m-%d %H:%M")
                    
                    if post['text'] and time_difference < timedelta(days=timedelta_days):
                        all_posts.append(post)
                    else:
                        continue

                all_posts.sort(key=lambda x: datetime.strptime(x["date"], "%Y-%m-%d %H:%M"), reverse=True)

            except Exception as e:
                print(f"Error fetching posts from {channel}: {e}")


        return all_posts


async def main():
    posts = await get_news()
    return posts


if __name__ == "__main__":
    print(asyncio.run(main()))
