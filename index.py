# This is the driver code for onboarding 
from variables import *

def main():
    import sys
    import time

    sys.path.append('\\'.join(sys.path[0].split('\\')[:-1]))


    from Scripts.availabilityAndUpdatePlan import addAvailabilityAndUpdatePlan
    from Scripts.addProperty import addProperty
    from Scripts.addRoom import addRoom
    from Scripts.addSubscription import addSubscription
    from Scripts.businessService import businessServiceApi
    from Scripts.login import login
    from Scripts.pointOfSale import pointOfSaleApi
    from Scripts.roomInfo import roomInformation
    from Scripts.roomPlan import addRoomPlan
    from Scripts.signUp import signUp
    from Scripts.updateUser import updateUser
    from Scripts.yearlyGenerate import yearlyGenerateApi

    count=1

    for x in jsonData:
        # JSON READ
        print('ONBOARDING STARTS FOR PROPERTY -- >', count)
        print()

        # 1-SIGN UP API
        signUpStatusCode = signUp(businessEmail,password)

        if signUpStatusCode == 201 or signUpStatusCode == 226:
            # LOGIN API CALL
            data = login(businessEmail, password)

            userId = data['userId']
            t = data['token']
            apiToken = f'Bearer {t}'
            loginStatusCode = data['status-code']

        time.sleep(2)

        if loginStatusCode == 200:
            # 2-UPDATE USER API
            updateUserApiStatusCode=updateUser(userId)

        time.sleep(2)

        header = {
            'USER_ID': str(userId),
            'Authorization': apiToken,
            'APP_ID': 'BOOKONE_WEB_APP'
        }

        time.sleep(2)

        if updateUserApiStatusCode == 200:
            # ADD PROPERTY API
            addPropertyApi=addProperty(header,userId)
            propertyId=addPropertyApi['propertyId']
            addPropertyStatusCode=addPropertyApi['status']

        time.sleep(2)

        if addPropertyStatusCode == 200:
            # ADD SUBSCRIPTION API
            subscriptionStatusCode=addSubscription(propertyId,userId,header)

        time.sleep(2)

        if subscriptionStatusCode == 200:
            # ADD ROOM API
            addRoomApiStatusCode=addRoom(propertyId,header)

        time.sleep(2)

        if addRoomApiStatusCode == 201:
            allRoomIdList = roomInformation(propertyId,header)
            # ADD ROOM PLAN API
            time.sleep(2)
            addPlan=addRoomPlan(allRoomIdList,propertyId,header)

            time.sleep(2)
            availbilityAndUpdatePlanApi=addAvailabilityAndUpdatePlan(allRoomIdList,propertyId,header)
            
        time.sleep(2)

        yearlyGenerate=yearlyGenerateApi(propertyId,header)

        time.sleep(2)

        pos=pointOfSaleApi(propertyId,header)

        time.sleep(2)

        addBusinessService=businessServiceApi(propertyId,header)
        
        count=count+1
        print('-----------------------------------------------------------------------------------------------------')


    