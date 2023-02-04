import json
import requests
from variables import *
import helper

config=helper.read_config()

s=requests.Session()

def roomInformation(propertyId,header):
    # GET ROOM ID

    if env_variable == 'TEST':
        getRoomDetailsApi=config['TestApi']['getroomdetailsapi'].replace('{propertyId}',str(propertyId))
    elif env_variable == 'PRODUCTION':
        getRoomDetailsApi=config['ProductionApi']['getroomdetailsapi'].replace('{propertyId}',str(propertyId))

    getRoomDetailsApiCall = s.get(getRoomDetailsApi, headers=header)
    getRoomDetailsApiStatusCode = getRoomDetailsApiCall.status_code
    if getRoomDetailsApiStatusCode == 200:
        print('FETCHED ROOM DETAILS.')
    
    roomData = json.loads(getRoomDetailsApiCall.content)
    roomIdList = []
    for i in range(0, len(roomData)):
        roomIdList.append(roomData[i]['id'])

    return roomIdList