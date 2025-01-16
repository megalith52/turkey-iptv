import requests
import re

url = 'https://www.teve2.com.tr/canli-yayin'

response = requests.get(url, verify=True)  # SSL doğrulamasını açık bırakıyoruz.

if response.status_code == 200:
    match = re.search(r'"contentUrl"\s*:\s*"([^"]+)"', response.text)

    if match:
        video_url = match.group(1)
        print("TEVE2:", video_url)
    else:
        print("Video URL bulunamadı.")
else:
    print(f"İçerik alınamadı. HTTP Durum kodu: {response.status_code}")
