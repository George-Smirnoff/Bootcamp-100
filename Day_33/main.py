# importing the requests library
import requests


def main():
    # api-endpoint
    URL = "http://api.open-notify.org/iss-now.json"

    # sending get request and saving the response as response object
    r = requests.get(url=URL)
    r.raise_for_status()

    # extracting data in json format
    data = r.json()

    # extracting latitude, longitude and formatted address
    # of the first matching location
    if data.get('message') == 'success':
        latitude = data['iss_position']['latitude']
        longitude = data['iss_position']['longitude']

    # printing the output
    print(f"Latitude: {latitude}\n"
          f"Longitude: {longitude}")



if __name__ == '__main__':
    main()
