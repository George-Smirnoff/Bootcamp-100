# importing the requests library
import time
from datetime import datetime
from math import isclose
import requests
import smtplib
import os

def send_iss_email():
    mail_content = 'Subject: Look UP!\n\nThe ISS is above you in the sky!!!'

    #The mail addresses and password
    sender_address = os.getenv('GMAIL_LOGIN')
    sender_pass = os.getenv('GMAIL_PWD')
    receiver_address = os.getenv('TARGET_EMAIL')
    connection = smtplib.SMTP('smtp.gmail.com')
    connection.starttls()
    connection.login(user=sender_address, password=sender_pass)
    connection.sendmail(
        from_addr=sender_address,
        to_addrs=receiver_address,
        msg=mail_content
    )
    print(f"Mail Sent to {receiver_address}.")


def iss_close(latitude):
    # api-endpoint
    issURL = "http://api.open-notify.org/iss-now.json"

    # sending get request and saving the response as response object
    issResponse = requests.get(url=issURL)
    issResponse.raise_for_status()

    # extracting data in json format
    issData = issResponse.json()

    # extracting latitude, longitude and formatted address
    # of the first matching location
    if issData.get('message') == 'success':
        issLatitude = float(issData['iss_position']['latitude'])

    # myLatitude and issLatitude within +5 or -5 range
    if isclose(latitude, issLatitude, abs_tol=5):
        return True


def its_dark(latitude, longitude):
    # URL to get sunrise/sunset data
    sunURL = 'https://api.sunrise-sunset.org/json'
    parameters = {
        'lat': latitude,
        'lng': longitude,
        'formatted': 0
    }
    response = requests.get(url=sunURL, params=parameters)
    response.raise_for_status()
    sun_data = response.json()

    # Extract sunrise/sunset time
    sunrise = sun_data['results']['sunrise']
    sunset = sun_data['results']['sunset']

    # Extract the sunrise/sunset hours
    sunriseHour = int(sunrise.split('T')[1].split(':')[0])
    sunsetHour = int(sunset.split('T')[1].split(':')[0])
    hour = datetime.now().hour

    # check if it's dark
    if hour <= sunriseHour or hour >= sunsetHour:
        return True


def main():
    # my coordinates
    myLatitude = 43.3640
    myLongitude = 150.7005

    while True:
        if iss_close(myLatitude) and its_dark(myLatitude, myLongitude):
            send_iss_email()
        time.sleep(60)


if __name__ == '__main__':
    main()
