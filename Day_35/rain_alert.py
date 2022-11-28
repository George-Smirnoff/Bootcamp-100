import requests
import os
from twilio.rest import Client

def main():
    url = "https://api.openweathermap.org/data/2.5/forecast"

    myLatitude = 48.8588548
    myLongitude = 2.347035
    send_sms = False
    api_key = os.getenv('API_KEY')

    parameters = {
        'lat': myLatitude,
        'lon': myLongitude,
        'appid': api_key
    }

    r = requests.get(url=url, params=parameters)

    weatherData = r.json()

    weatherList = weatherData["list"]
    for item in weatherList[:4]:
        if item["weather"][0]["id"] < 600:
            print(f'RAINY! at {item["dt_txt"]}')
            send_sms = True

    if send_sms:
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        caller_phone = os.environ['TWILIO_PHONE_NUMBER']
        target_phone = os.environ['TARGET_PHONE_NUMBER']
        client = Client(account_sid, auth_token)

        client.messages.create(
            body='Hello,\nWe are expecting a rain this day. Take your umbrella!',
            from_=caller_phone,
            to=target_phone
        )
        print('Message sent.')

if __name__ == '__main__':
    main()