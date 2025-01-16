import requests

ntv_base_url = "https://mn-nl.mncdn.com/dogusdyg_ntv/"
initial_url = "https://dygvideo.dygdigital.com/live/hls/kralpop?m3u8"

def log_1080p_stream(base_url, modified_url):
    try:
        content_response = requests.get(modified_url)
        content_response.raise_for_status()
        content = content_response.text

        lines = content.split("\n")
        for i in range(len(lines)):
            if "RESOLUTION=1920x1080" in lines[i]:
                full_url = lines[i + 1].strip()
                if not full_url.startswith("http"):
                    full_url = base_url + full_url
                
                print("NTV:", full_url)
                return
        
        print("1080p stream not found in the content.")

    except requests.RequestException as e:
        print(f"An error occurred while fetching {modified_url}: {e}")

try:
    response = requests.get(initial_url)
    response.raise_for_status()

    final_url = response.url
    ntv_modified_url = final_url.replace("dogusdyg_kralpoptv/dogusdyg_kralpoptv.smil/playlist", "dogusdyg_ntv/live")

    log_1080p_stream(ntv_base_url, ntv_modified_url)

except requests.RequestException as e:
    print(f"An error occurred while fetching the initial URL: {e}")
