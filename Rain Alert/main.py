import requests
from twilio.rest import Client

parameters = {
    'lat': -34.629699,
    'lon': -58.461846,
    'cnt': 1,
    'appid': "b99dd81ac0d7baf983175feabbc8c24b"
}

API = "https://api.openweathermap.org/data/2.5/forecast"

account_sid = "AC876aa6f19306177801886b41ae54c6da"
auth_token = "a9325d1c38cf5bac479c49f132539eef"

response = requests.get(API, params=parameters)
response.raise_for_status()
weather_data = response.json()

id_weather = weather_data['list'][0]['weather'][0]['id']

if id_weather < 700:
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body="It's going to rain today. Remember to bring an umbrella.",
                        from_='+PHONE NUMBER FROM TWILIO',
                        to='+PHONE NUMBER TO SEND'
                    )

    print(message.status)

else:
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body="It's going to be sunny today. Remember to use sunscreen.",
                        from_='+PHONE NUMBER FROM TWILIO',
                        to='+PHONE NUMBER TO SEND'
                    )

    print(message.status)