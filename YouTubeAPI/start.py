import re
from datetime import timedelta

from config import api_key
from googleapiclient.discovery import build

yt = build('youtube', 'v3', developerKey=api_key)

nxtPageToken = None

hrs_pattern = re.compile(r'(\d+)H')
min_pattern = re.compile(r'(\d+)M')
sec_pattern = re.compile(r'(\d+)S')

total_secs = 0

url = input("Enter the url of the playlist :")
if len(url) < 1:
    url = "https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU"

if "list=" not in url:
    raise Exception("Enter valid url")


url = url.split("list=")
pl_id = url[1]
# print(url)
pl_title = None

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
        part='contentDetails',
        id=','.join(vid_ids)
    )

    res_vid = req_vid.execute()

    for item in res_vid['items']:
        duration = item['contentDetails']['duration']
        hrs = hrs_pattern.search(duration)
        mins = min_pattern.search(duration)
        secs = sec_pattern.search(duration)

        hrs = int(hrs_pattern.search(duration).group(1)) if hrs else 0
        mins = int(min_pattern.search(duration).group(1)) if mins else 0
        secs = int(sec_pattern.search(duration).group(1)) if secs else 0

        vid_secs = timedelta(
            hours=hrs,
            minutes=mins,
            seconds=secs
        ).total_seconds()

        total_secs += vid_secs

    nxtPageToken = res_pl.get('nextPageToken')
    if not nxtPageToken:
        break

total_secs = int(total_secs)

mins, secs = divmod(total_secs, 60)
hrs, mins = divmod(mins, 60)

print(hrs, mins, secs, sep=":")
