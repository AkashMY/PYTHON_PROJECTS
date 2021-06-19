import requests
from twilio.rest import Client

My_latitude = 16.717840
My_longitude = 75.084473

account_sid = "AC1eae4c1499721ed1fcd2e1b196a6baf8"
auth_token = "71a89242cc2eb3fcc269a673ae379320"

app_key = "5288a0cc9e9ecc311c26579bf13c2104"

parameters = {
    "lat": My_latitude,
    "lon": My_longitude,
    "exclude": "current,minutely,daily,alerts",
    "appid": app_key,
}

responce = requests.get(url="https://api.openweathermap.org/data/2.5/onecall?", params=parameters)
responce.raise_for_status()

# weather = responce.json()["hourly"][0]["weather"][0]["id"]

weather_slice_11hrs = responce.json()["hourly"][:12]

is_rains = False

for item in weather_slice_11hrs:
    condition_code = item["weather"][0]["id"]
    if condition_code < 700:
        is_rains = True

client = Client(account_sid, auth_token)

if is_rains:
    message = client.messages \
        .create(
          body="It's going to rain today, Remember to bring Umbrella☂",
          from_='+19893422211',
          to='+919008811801'
        )
        

print(message.status)
