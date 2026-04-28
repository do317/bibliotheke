import requests

# aizsūta HTTP 'GET' uz kādu saiti
# ar `data` argumentu var iedod arguments saitei
print(requests.get('http://google.com', data={"a":"33"}))
