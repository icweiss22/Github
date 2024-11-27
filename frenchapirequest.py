import requests

def send_request():
    word = "lune"
    url = f"https://api.dictionaryapi.dev/api/v2/entries/fr/{word}"

    response = requests.get(url)
    if response.ok:
        data = response.json()
        print(data)
    else:
        print(response)

if __name__ == "__main__":
    send_request()