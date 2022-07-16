import requests
def load_url(url):
    response = requests.get(url)
    return response.text