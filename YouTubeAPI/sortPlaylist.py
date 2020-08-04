from config import api_key
from googleapiclient.discovery import build

yt = build('youtube', 'v3', developerKey=api_key)

nxtPageToken = None


url = input("Enter the url of the playlist :")
if len(url) < 1:
    url = "https://www.youtube.com/playlist?list=PL8uoeex94UhHFRew8gzfFJHIpRFWyY4YW"

if "list=" not in url:
    raise Exception("Enter valid url")


url = url.split("list=")
pl_id = url[1]

videos = []

while True:
    req_pl = yt.playlistItems().list(
        part='contentDetails',
        playlistId=pl_id,
        maxResults=50,
        pageToken=nxtPageToken
    )

    res_pl = req_pl.execute()

    vid_ids = []

    for item in res_pl['items']:
        vid_ids.append(item['contentDetails']['videoId'])

    req_vid = yt.videos().list(
        part='statistics',
        id=','.join(vid_ids)
    )

    res_vid = req_vid.execute()

    for item in res_vid['items']:
        vid_views = item['statistics']['viewCount']

        vid_id = item['id']
        yt_link = f'https://youtu.be/{vid_id}'

        videos.append(
            {
                'views': int(vid_views),
                'url': yt_link
            }
        )

    nxtPageToken = res_pl.get('nextPageToken')

    if not nxtPageToken:
        break

videos.sort(key=lambda vid: vid["views"], reverse=True)

for video in videos[:10]:
    print(video['url'], video['views'])

print(len(videos))
