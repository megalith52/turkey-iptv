import requests
import re

url = 'https://halktv.com.tr/canli-yayin'

response = requests.get(url, verify=False)

if response.status_code == 200:
    match = re.search(r'var\s+videoUrl\s*=\s*"(https?://[^"]+)"', response.text)
  
    if match:
        erstrm = match.group(1)
        print("HALKTV:", erstrm)
    else:
        print("erstrm not found in the content.")
else:
    print(f"Failed to fetch content. HTTP Status code: {response.status_code}")