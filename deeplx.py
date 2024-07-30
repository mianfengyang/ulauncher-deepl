import httpx, json


deeplx_api = "http://127.0.0.1:1188/translate"

data = {
	"text": "Hello World",
	"source_lang": "EN",
	"target_lang": "ZH"
}

post_data = json.dumps(data)

def translation(query):
    items = []
    rt = httpx.post(url = deeplx_api, data = query).json()
    items.append(dict(
        title = rt["data"],
        source_lang=rt["source_lang"],
        target_lang=rt["target_lang"],
        icon = "images/icon.png"
	))
    return items

if __name__ == '__main__':
	r = translation(post_data)
	print(r)