import httpx, json


def translation():
    deeplx_api = "http://192.168.1.7:1188/translate"
    
    content = input("eg. en:zh hello: ")
    while content != "q":
        #data = {
        #    "text": content.split(" ")[1],
        #    "source_lang": content.split(" ")[0].split(":")[0].upper(),
        #    "target_lang": content.split(" ")[0].split(":")[1].upper(),
        #}
        data = {
            "text": content.split(" ")[1],
            "source_lang": "auto",
            "target_lang": content.split(" ")[0].split(":")[1].upper(),
        }
        query = json.dumps(data)
        rt = httpx.post(url = deeplx_api, data = query).json()
        if rt["alternatives"] != None:
            rt["alternatives"].append(rt["data"])
            for i in rt["alternatives"]:
                print(i)
        else:
            print(rt["data"])
        content = input("eg. en:zh hello: ")


if __name__ == '__main__':
    translation()
  