import requests
from variables import *
from datetime import date, timedelta
import helper

config=helper.read_config()

s=requests.Session()

def addAvailabilityAndUpdatePlan(allRoomIdList,propertyId,header):

    allRoomPlans = roomPlan.split(',')

    if len(allRoomIdList) == len(allRoomPlans):
        for i in range(0, len(allRoomIdList)):
            # ADD AVAILABILITY BY DATE RANGE API
            individualRoomId = allRoomIdList[i]

            fromDate = date.today()
            timeSpan = timedelta(days=30) 
            # for 1 month 
            toDate = fromDate+timeSpan

            if env_variable == 'TEST':
                addAvailabilityByDate=config['TestApi']['addavailabilitybydate']
            elif env_variable == 'PRODUCTION':
                addAvailabilityByDate=config['ProductionApi']['addavailabilitybydate']

            addAvailabilityDto = {
                "roomId": individualRoomId,
                "propertyId": propertyId,
                "price": '500',
                "noOfRooms": '',
                "fromDate": str(fromDate),
                "toDate": str(toDate)
            }

            addAvailabilityByDateApi = s.post(
                addAvailabilityByDate, json=addAvailabilityDto, headers=header)

            if addAvailabilityByDateApi.status_code == 200:
                print('Add availability by date range api status code',addAvailabilityByDateApi.status_code)

                if env_variable == 'TEST':
                    addOrUpdatePlanApi=config['TestApi']['addorupdateplanapi']
                elif env_variable == 'PRODUCTION':
                    addOrUpdatePlanApi=config['ProductionApi']['addorupdateplanapi']

                addOrUpdatePlanPayload = {
                    "code": "C1",
                    "name": allRoomPlans[i],
                    "effectiveDate": str(fromDate),
                    "expiryDate": str(toDate),
                    "description": None,
                    "active": True,
                    "applicableToOta": None,
                    "amount": '',
                    "roomId": individualRoomId,
                    "deviationFromStandardPlan": 0,
                    "minimumLengthOfStay": 1,
                    "maximumLengthOfStay": 999,
                    "status": "Open",
                    "restriction": "None",
                    "currencyCode": "INR",
                    "minimumOccupancy": 2,
                    "maximumOccupancy": 4,
                    "extraChargePerPerson": 1000,
                    "extraChargePerChild": 500,
                    "extraChargePerChild3To5yrs": 100,
                    "noOfChildren": 0,
                    "dayOfTheWeekList": [
                        "MONDAY",
                        "TUESDAY",
                        "WEDNESDAY",
                        "THURSDAY",
                        "SATURDAY",
                        "FRIDAY"
                    ],
                    "propertyServicesList": [],
                    "onedayPlan": None,
                    "channelManagerUpdateType": "ROOM_RATE_PLAN",
                    "propertyId": propertyId,
                    "roomTypeId": individualRoomId
                }

                addOrUpdateApiCall = s.post(
                    addOrUpdatePlanApi, json=addOrUpdatePlanPayload, headers=header)

                if addOrUpdateApiCall.status_code == 200:
                    print('Add or update plan api status code',addOrUpdateApiCall.status_code)
                elif addOrUpdateApiCall.status_code == 500:
                    print('Add or update plan api status code',addOrUpdateApiCall.status_code)

            elif addAvailabilityByDateApi.status_code == 500:
                print('Add availability by date range api status code',addAvailabilityByDateApi.status_code)

    elif len(allRoomPlans) == 1:
        for i in range(0, len(allRoomIdList)):
            # ADD AVAILABILITY BY DATE RANGE API
            individualRoomId = allRoomIdList[i]
            
            fromDate = date.today()
            timeSpan = timedelta(days=30) 
            # for 1 month 
            toDate = fromDate+timeSpan

            if env_variable == 'TEST':
                addAvailabilityByDate=config['TestApi']['addavailabilitybydate']
            elif env_variable == 'PRODUCTION':
                addAvailabilityByDate=config['ProductionApi']['addavailabilitybydate']

            addAvailabilityDto = {
                "roomId": individualRoomId,
                "propertyId": propertyId,
                "price": '500',
                "noOfRooms": '',
                "fromDate": str(fromDate),
                "toDate": str(toDate)
            }

            addAvailabilityByDateApi = s.post(
                addAvailabilityByDate, json=addAvailabilityDto, headers=header)

            if addAvailabilityByDateApi.status_code == 200:
                print('Add availability by date range api status code',addAvailabilityByDateApi.status_code)

                if env_variable == 'TEST':
                    addOrUpdatePlanApi=config['TestApi']['addorupdateplanapi']
                elif env_variable == 'PRODUCTION':
                    addOrUpdatePlanApi=config['ProductionApi']['addorupdateplanapi']

                addOrUpdatePlanPayload = {
                    "code": "C1",
                    "name": allRoomPlans[0],
                    "effectiveDate": str(fromDate),
                    "expiryDate": str(toDate),
                    "description": None,
                    "active": True,
                    "applicableToOta": None,
                    "amount": '',
                    "roomId": individualRoomId,
                    "deviationFromStandardPlan": 0,
                    "minimumLengthOfStay": 1,
                    "maximumLengthOfStay": 999,
                    "status": "Open",
                    "restriction": "None",
                    "currencyCode": "INR",
                    "minimumOccupancy": 2,
                    "maximumOccupancy": 4,
                    "extraChargePerPerson": 1000,
                    "extraChargePerChild": 500,
                    "extraChargePerChild3To5yrs": 100,
                    "noOfChildren": 0,
                    "dayOfTheWeekList": [
                        "MONDAY",
                        "TUESDAY",
                        "WEDNESDAY",
                        "THURSDAY",
                        "SATURDAY",
                        "FRIDAY"
                    ],
                    "propertyServicesList": [],
                    "onedayPlan": None,
                    "channelManagerUpdateType": "ROOM_RATE_PLAN",
                    "propertyId": propertyId,
                    "roomTypeId": individualRoomId
                }

                addOrUpdateApiCall = s.post(
                    addOrUpdatePlanApi, json=addOrUpdatePlanPayload, headers=header)

                if addOrUpdateApiCall.status_code == 200:
                    print('Add or update plan api status code',addOrUpdateApiCall.status_code)
                elif addOrUpdateApiCall.status_code == 500:
                    print('Add or update plan api status code',addOrUpdateApiCall.status_code)

            elif addAvailabilityByDateApi.status_code == 500:
                print('Add availability by date range api status code',addAvailabilityByDateApi.status_code)

    return None