import requests

def get_word_of_the_day():
    response = requests.get('https://api.wordnik.com/v4/words.json/wordOfTheDay?api_key=YOUR_API_KEY')
    if response.status_code != 200:
        raise Exception('Network response was not ok ' + response.reason)
    data = response.json()
    print(f"Word of the Day: {data['word']}")
    print(f"Meaning: {data['definitions'][0]['text']}")

try:
    get_word_of_the_day()
except Exception as error:
    print('Error fetching the word of the day:', error)