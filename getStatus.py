#!/bin/python3

import requests
import json
import config



target_ip = routerIp

headers = {'Accept-Language': 'en'}
url='http://{host}/data/'.format(host=target_ip)

def logIn(Username, password):
	action_endpoint = "Login.json"
	action_url=url + action_endpoint
	data = {
	'showpw': '0',
	'username': Username,
	'password': password
	}
	session= requests.session()
	response = session.post(action_url, headers=headers, data=data)
	return response.cookies.get_dict()["session_id"]


def getStatus(session_id):
	action_endpoint = "Status.json"
	action_url=url + action_endpoint
	headers = {'Accept-Language': 'en','Cookie':'session_id={cookie}'.format(cookie=session_id)}
	request = requests.get(action_url, headers=headers)
	# print(json.dumps(request.json(), indent=4, sort_keys=True), file=open('my_router_responses/Status.json', "a"))
	json_data = json.loads(request.text)
	return json_data

# print(logIn(Username,password))

sesid= logIn(Username,password)
print (sesid)

print (getStatus(sesid))