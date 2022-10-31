# importing the requests library
from datetime import datetime
from math import isclose
import requests
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_iss_email():
    mail_content = 'Wake UP! ISS is very close and you can see that!!!'

    #The mail addresses and password
    sender_address = os.getenv('GMAIL_LOGIN')
    sender_pass = os.getenv('GMAIL_PWD')
    receiver_address = os.getenv('TARGET_EMAIL')
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'ISS is close'   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print(f"Mail Sent to {receiver_address}.")

def main():
    # my coordinates
    myLatitude = 52.5425303
    myLongitude = 13.4940118

    # api-endpoint
    issURL = "http://api.open-notify.org/iss-now.json"

    # sending get request and saving the response as response object
    issResponse = requests.get(url=issURL)
    issResponse.raise_for_status()

    # extracting data in json format
    issData = issResponse.json()

    # extracting latitude, longitude and formatted address
    # of the first matching location
    if issData.get('message')== 'success':
        issLatitude = float(issData['iss_position']['latitude'])
        issLongitude = float(issData['iss_position']['longitude'])

    # printing the output
    # print(f"Latitude: {latitude}\n"
    #       f"Longitude: {longitude}")

    sunURL = 'https://api.sunrise-sunset.org/json'
    parameters = {
        'lat': myLatitude,
        'lng': myLongitude,
        'formatted': 0
    }
    # Or you can provide the dict() to 'params' option
    #1 response = requests.get(url=sunURL, params=f"lat={myLatitude}&lng={myLongitude}")
    response = requests.get(url=sunURL, params=parameters)
    response.raise_for_status()
    sun_data = response.json()

    sunrise = sun_data['results']['sunrise']
    sunset = sun_data['results']['sunset']
    sunriseHour = int(sunrise.split('T')[1].split(':')[0])
    sunsetHour = int(sunset.split('T')[1].split(':')[0])
    #1 hour = datetime.now().strftime("%H")
    #1 second = datetime.now().strftime("%S")
    hour = datetime.now().hour
    second = datetime.now().second

    # myLatitude and issLatitude within +5 or -5 range
    if isclose(myLatitude, issLatitude, abs_tol=5):
        if hour <= sunriseHour or hour >= sunsetHour:
            send_iss_email()


if __name__ == '__main__':
    main()
