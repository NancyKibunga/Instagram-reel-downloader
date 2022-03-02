from instascrape import Reel
import time

SESSIONID = "17f4c0258bf-db0f5c"

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
	AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 \
	Safari/537.36 Edg/79.0.309.43",
	"cookie": f'sessionid={SESSIONID};'
}

insta_reel = Reel(
	'https://www.instagram.com/reel/CakctnGKdt5/?utm_source=ig_web_copy_link')

insta_reel.scrape(headers=headers)

insta_reel.download(fp=f".\\Desktop\\reel{int(time.time())}.mp4")

print('Reel downloaded successfully!')