import requests
from twilio.rest import Client

OMW_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "you open weather map api key"

account_sid = "you twilio account sid"
auth_token = "your twilio auth token"

weather_params = {
    "lat":28.474388,
    "lon":77.503990,
    "appid":api_key,
    "cnt":4
}

response = requests.get(OMW_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

#print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
    
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's Gonna rain today. So remember to bring an Umbrella! ⛈️☂️",
        from_="+19123616563",
        to="+919289419730",
    )
    print(message.status)