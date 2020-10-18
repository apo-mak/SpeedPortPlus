#!/bin/python3

import requests
import json
import config

target_ip = config.routerIp

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
	json_data = request.json()
	return json_data



def json_to_dic(json_data):
	results_dic= {}
    
	for v in json_data:
		results_dic[v["varid"]] = v["varvalue"]
	return results_dic


sesid= logIn(config.Username,config.password)

data_from_request= getStatus(sesid)


print ( json_to_dic(data_from_request)["router_state"])
