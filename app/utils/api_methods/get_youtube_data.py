import scrapetube

async def get_youtube_videos():
    with open(file='app/my_subscriptions.txt', mode='r', encoding='utf-8') as my_subscriptions:
        channel_usernames = my_subscriptions.read().split('\n')

    all_videos = []

    for channel_username in channel_usernames:
        videos = scrapetube.get_channel(channel_username=channel_username, limit=1, content_type='videos')

        try:
            for video in videos:
                if 'day' not in video['publishedTimeText']['simpleText'] and 'month' not in video['publishedTimeText']['simpleText'] and 'week' not in video['publishedTimeText']['simpleText'] and 'year' not in video['publishedTimeText']['simpleText']:
                    all_videos.append(
                        {
                            'title': video['title']['runs'][0]['text'],
                            'date': video['publishedTimeText']['simpleText'],
                            'views': video['viewCountText']['simpleText'],
                            'duration': video['lengthText']['simpleText'],
                            'url': f'https://www.youtube.com/watch?v={video['videoId']}',
                            'preview_url': video['thumbnail']['thumbnails'][3]['url'],
                            'channel': channel_username
                        }
                    )
        except Exception as error:
            return error

    return all_videos
