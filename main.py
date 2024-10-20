import requests



if __name__ == '__main__':
    url = "https://www.zhihu.com/hot"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
    }
    response = requests.get(url=url, headers=headers)
    
    if response.status_code == 200:
        print(response.content)
    else:
        print(f"请求失败！{response.status_code}")
