import requests
from variables import *
from datetime import date, timedelta
import helper

config=helper.read_config()

s=requests.Session()

def addRoomPlan(allRoomIdList,propertyId,header):

    allRoomPlans = roomPlan.split(',')
    effectiveDate = date.today()
    timeDiff = timedelta(days=30)
    expiryDate = effectiveDate+timeDiff

    if len(allRoomIdList) == len(allRoomPlans):
        for i in range(0, len(allRoomIdList)):
            individualRoomId = allRoomIdList[i]
            
            if env_variable == 'TEST':
                roomPlanApi=config['TestApi']['addroomplanapi'].replace('{propertyId}',str(propertyId)).replace('{individualRoomId}',str(individualRoomId))
            elif env_variable == 'PRODUCTION':
                roomPlanApi=config['ProductionApi']['addroomplanapi'].replace('{propertyId}',str(propertyId)).replace('{individualRoomId}',str(individualRoomId))

            roomPlanPayload = {
                "dayOfTheWeekList": [
                    "MONDAY",
                    "TUESDAY",
                    "WEDNESDAY",
                    "THURSDAY",
                    "SATURDAY",
                    "FRIDAY"
                ],
                "status": "Open",
                "maximumLengthOfStay": 999,
                "minimumLengthOfStay": 1,
                "restriction": "None",
                "code": "C1",
                "name": allRoomPlans[i],
                "minimumOccupancy": 2,
                "maximumOccupancy": 4,
                "extraChargePerPerson": 1000,
                "noOfChildren": 0,
                "extraChargePerChild3To5yrs": 100,
                "extraChargePerChild": 500,
                "effectiveDate": str(effectiveDate),
                "expiryDate": str(expiryDate),
                "currencyCode": "INR",
                "amount": '500',
                "active": True,
                "propertyId": propertyId,
                "roomTypeId": individualRoomId,
                "deviationFromStandardPlan": 0
            }

            roomPlanApiRes = s.post(
                roomPlanApi, json=roomPlanPayload, headers=header)
            roomPlanApiStatusCode = roomPlanApiRes.status_code
            if roomPlanApiStatusCode ==  201:
                print('Add room plan api status code',roomPlanApiStatusCode,'for plan ',i+1)

    elif len(allRoomPlans) == 1:
        for i in range(0, len(allRoomIdList)):
            individualRoomId = allRoomIdList[i]

            if env_variable == 'TEST':
                roomPlanApi=config['TestApi']['addroomplanapi'].replace('{propertyId}',str(propertyId)).replace('{individualRoomId}',str(individualRoomId))
            elif env_variable == 'PRODUCTION':
                roomPlanApi=config['ProductionApi']['addroomplanapi'].replace('{propertyId}',str(propertyId)).replace('{individualRoomId}',str(individualRoomId))

            roomPlanPayload = {
                "dayOfTheWeekList": [
                    "MONDAY",
                    "TUESDAY",
                    "WEDNESDAY",
                    "THURSDAY",
                    "SATURDAY",
                    "FRIDAY"
                ],
                "status": "Open",
                "maximumLengthOfStay": 999,
                "minimumLengthOfStay": 1,
                "restriction": "None",
                "code": "C1",
                "name": allRoomPlans[0],
                "minimumOccupancy": 2,
                "maximumOccupancy": 4,
                "extraChargePerPerson": 1000,
                "noOfChildren": 0,
                "extraChargePerChild3To5yrs": 100,
                "extraChargePerChild": 500,
                "effectiveDate": str(effectiveDate),
                "expiryDate": str(expiryDate),
                "currencyCode": "INR",
                "amount": '500',
                "active": True,
                "propertyId": propertyId,
                "roomTypeId": individualRoomId,
                "deviationFromStandardPlan": 0
            }

            roomPlanApiRes = s.post(
                roomPlanApi, json=roomPlanPayload, headers=header)
            roomPlanApiStatusCode = roomPlanApiRes.status_code
            if roomPlanApiStatusCode ==  201:
                print('Add room plan api status code',roomPlanApiStatusCode,'for plan ',i+1)


    return roomPlanApiStatusCode
