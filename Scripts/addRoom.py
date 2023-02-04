import requests
from variables import *
import helper

config=helper.read_config()

s=requests.Session()

def addRoom(propertyId,header):

    if env_variable == 'TEST':
        addRoomApi=config['TestApi']['addroomapi'].replace('{propertyId}',str(propertyId))
    elif env_variable == 'PRODUCTION':
        addRoomApi=config['ProductionApi']['addroomapi'].replace('{propertyId}',str(propertyId))

    typesOfRoom = roomType.split(',')

    for i in range(0, len(typesOfRoom)):
        addRoomPayload = {
            "dayTrip": False,
            "name": typesOfRoom[i],
            "noOfRooms": 2,
            "roomOnlyPrice": 500,
            "minimumOccupancy": 2,
            "maximumOccupancy": 3,
            "roomFacilities": [
                {
                    "id": 1001,
                    "organisationId": 1,
                    "name": "Wifi",
                    "description": "Wifi",
                    "logoUrl": "https://bookonelocal.in/cdn/2021-06-22-103115784-wifi.png",
                    "imageUrl": "https://bookonelocal.in/cdn/2021-06-22-103124170-wifi.png"
                }
            ],
            "propertyId": propertyId
        }

        addRoomApiRes = s.post(
            addRoomApi, json=addRoomPayload, headers=header)
        if addRoomApiRes.status_code == 201:
            print('Add room api status code',addRoomApiRes.status_code ,'for room type ',i+1)

    return addRoomApiRes.status_code