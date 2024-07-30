import httpx, json


deeplx_api = "http://127.0.0.1:1188/translate"

data = {
	"text": "你是从哪里来的，将要去哪里，我是谁",
	"source_lang": "ZH",
	"target_lang": "EN"
}

post_data = json.dumps(data)

def translation(query):
    rt = httpx.post(url = deeplx_api, data = query).json()
    print(rt)
    return rt

if __name__ == '__main__':
	r = translation(post_data)
	print(r)