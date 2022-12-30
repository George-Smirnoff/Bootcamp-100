# import json
import os
import pandas as pd
import requests
import random
import string
import re
import time

URL = 'https://pixe.la/v1/users'
PWD_LENGHT = 24
CRED_PATH = 'creds.json'


# Generate secret
def secret_gen():
    password = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in range(PWD_LENGHT)])
    pattern = re.compile("[ -~]{8,128}")
    if bool(pattern.match(password)):
        return password
    else:
        print(f"Wrong secret format.")
        exit(0)


def createUser(name=None):
    if name is not None:
        pattern = re.compile("[a-z][a-z0-9-]{1,32}")
        if bool(pattern.match(name)):
            user_param = {
                'token': secret_gen(),
                'username': name,
                'agreeTermsOfService': 'yes',
                'notMinor': 'yes'
            }
            try:
                r = requests.post(url=URL, json=user_param)
                print(f"The user `{name}` was created")
            except:
                print(f"Failed to create user with username: {name}. Failed with error: {r.text}")
            try:
                df = pd.DataFrame(user_param, index=[0])
                df.to_json(CRED_PATH)
            except:
                print(f"Failed to save user credentials")
            return user_param
        else:
            print('The username does not match the pattern')

# def createGraph()

def main():
    # username = input("Create a user with name: ")
    if os.path.exists(CRED_PATH):
        df = pd.read_json(CRED_PATH)
        param = {}
        for elem in df:
            param[elem] = df[elem][0]
    else:
        param = createUser("ben2")


    # NOT OPTIMIZED CODE

    authHeader = {'X-USER-TOKEN': param['token']}
    graphId = "graph1"
    graph_body = {
        "id": graphId, # regexp
        "name": "heh1",
        "unit": "km",
        "type": "int",
        "color": "shibafu"

    }
    requests.post(url=URL + f"/{param['username']}/graphs", json=graph_body, headers=authHeader)
    # data_json = r.json()
    # print(data_json)

    today = time.strftime("%Y%m%d")

    requests.post(url=URL + f"/{param['username']}/graphs/{graphId}",
                      json={"date": today, "quantity": str(random.randint(1, 9))},
                      # or with data option, need to setup 'content-type' header manually
                      # data=json.dumps({"date": today, "quantity": str(random.randint(1, 9))}),
                      headers=authHeader)
    # print(r.text)

    requests.put(url=URL + f"/{param['username']}/graphs/{graphId}/{today}",
                  json={"quantity": str(random.randint(1, 20))},
                  headers=authHeader)


    if input(f"Do you want to remove the {graphId} graph?(yes/no): ") == "yes":
        r = requests.delete(url=URL + f"/{param['username']}/graphs/{graphId}",
                        headers=authHeader)
        if r.json()['isSuccess']:
            print(f"Graph {graphId} deleted...")

    if input(f"Do you want to remove user `{param['username']}`?(yes/no): ") == "yes":
        r = requests.delete(url=URL + f"/{param['username']}",
                        headers=authHeader)

        if r.json()['isSuccess']:
            print(f"User {param['username']} deleted...")

if __name__ == '__main__':
    main()