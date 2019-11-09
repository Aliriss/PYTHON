import requests
def getHTMLtext(url):
    try:
        r=requests.get("http://www.baidu.com")
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "error"
