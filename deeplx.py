import httpx, json

data = {
	"text": "helo my sister",
}
data = {
	"text": "hello my sister",
	"source": "auto",
	"target_lang": "zh",
}
input = "tr zh:en 你好漂亮"
input = "tr zh:en 你好美"
data = {
	"text": input.split(" ")[2],
	"source_lang": input.split(" ")[1].split(":")[0].upper(),
	"target_lang": input.split(" ")[1].split(":")[1].upper(),
}
post_data = json.dumps(data)

def translation(query):
    deeplx_api = "http://127.0.0.1:1188/translate"
    rt = httpx.post(url = deeplx_api, data = query).json()
    print(rt)
    return rt

if __name__ == '__main__':
    r = translation(post_data)
    for i in r["alternatives"]:
        print(i)
    print(r["data"] )