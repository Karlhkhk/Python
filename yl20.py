import requests

Soovitud = (input("Sisesta soovitud linn: "))
# API võtme ja linna nime määramine
Linn = (Soovitud)
api_key = "f4718da5798ba9aea22497d29515b83a"
url = f"https://api.openweathermap.org/data/2.5/weather?q={Linn}&appid={api_key}&units=metric"

# API päringu tegemine
response = requests.get(url)

# Vastuse kontrollimine
if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']

    print(f"Temperatuur: {Linn} {temperature} °C")
else:
    print("Viga andmete allalaadimisel:", response.status_code)