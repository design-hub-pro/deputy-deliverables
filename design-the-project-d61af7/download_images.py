import os, json, urllib.request, urllib.parse, ssl, random

UNSPLASH_API_KEY = 'buhc7QncQ0ZMcCjMWpJhQ-NIiIjmoNeFYE4IyOiCbVA'
ASSETS = 'assets'

ssl_ctx = ssl.create_default_context()


def download_image(query, filename, orientation='landscape'):
    os.makedirs(ASSETS, exist_ok=True)
    try:
        params = urllib.parse.urlencode({'query': query, 'per_page': 10, 'orientation': orientation})
        url = f'https://api.unsplash.com/search/photos?{params}'
        req = urllib.request.Request(url, headers={'Authorization': f'Client-ID {UNSPLASH_API_KEY}'})
        with urllib.request.urlopen(req, context=ssl_ctx, timeout=20) as resp:
            data = json.loads(resp.read().decode())
        if data.get('results'):
            pick = random.choice(data['results'])
            image_url = pick['urls']['regular']
            with urllib.request.urlopen(image_url, context=ssl_ctx, timeout=20) as img_resp:
                img_data = img_resp.read()
            path = os.path.join(ASSETS, filename)
            with open(path, 'wb') as f:
                f.write(img_data)
            print(f"Downloaded: {filename} (query: {query})")
            return True
        else:
            print(f"No results for {filename} ({query})")
    except Exception as e:
        print(f"Failed {filename} ({query}): {e}")
    return False


# Calm, sensory-friendly imagery — each a distinct query, avoiding saturated red/orange scenes
download_image('soft blue gradient calm minimal background', 'hero-bg.jpg')
download_image('person reading tablet quiet study soft light', 'program1.jpg')          # Knowledge Center
download_image('handmade ceramic pottery pastel craft studio', 'program2.jpg')          # Marketplace
download_image('diverse team inclusive modern office collaboration', 'program3.jpg')    # Employment
download_image('community volunteers group outdoors green park', 'program4.jpg')        # Volunteer
download_image('modern glass office building architecture calm', 'program5.jpg')        # Corporate Partners
download_image('parent and child holding hands supportive gentle', 'impact.jpg')        # Impact
download_image('young person working laptop technology soft calm', 'evolution.jpg')      # Evolution / story
download_image('abstract soft rounded shapes lavender teal texture', 'texture.jpg')      # Section accent

print("Done.")
