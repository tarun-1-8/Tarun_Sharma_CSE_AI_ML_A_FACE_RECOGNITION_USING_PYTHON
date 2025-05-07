pip install -r requirements.txt
import urllib.request
import os


celebrities = {
    "elon_musk": ["https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.vanityfair.com%2Fnews%2F2016%2F06%2Fthe-one-technology-that-terrifies-elon-musk&psig=AOvVaw28qi3bZhI74CnLIm9FTjdz&ust=1746001304789000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCJDSmu7n_IwDFQAAAAAdAAAAABAE"],
    "emma_watson": ["https://upload.wikimedia.org/wikipedia/commons/e/e4/Emma_Watson_2013.jpg"],
    "tom_holland": ["https://upload.wikimedia.org/wikipedia/commons/3/34/Tom_Holland_by_Gage_Skidmore_2.jpg"]
}

os.makedirs("dataset", exist_ok=True)

for name, urls in celebrities.items():
    for i, url in enumerate(urls):
        try:
            path = f"dataset/{name}_{i}.jpg"
            urllib.request.urlretrieve(url, path)
            print(f"Downloaded {path}")
        except Exception as e:
            print(f"Failed to download {url}: {e}")
