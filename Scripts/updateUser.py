import requests
from variables import *
import helper

config=helper.read_config()

s=requests.Session()

def updateUser(userId):

    if env_variable == 'TEST':
        updateUserApi=config['TestApi']['updateuserapi']
    elif env_variable == 'PRODUCTION':
        updateUserApi=config['ProductionApi']['updateuserapi']

    updateUserdata = {
        "plan": "Business Premium",
        "organisationId": 1,
        "businessType": businessType,
        "businessTypeGroup": "TRAVEL & TOURISM",
        "email": businessEmail,
        "password": password,
        "confirmPassword": password,
        "id": userId,
        "businessName": businessName,
        "firstName": '',
        "lastName": '',
        "landphoneNumber": "",
        "mobileNumber": mobileNumber,
        "address": {
            "city": city,
            "suburb": suburb,
            "streetNumber": "",
            "streetName": streetName,
            "country": country,
            "state": state,
            "postcode": postcode
        },
        "dashboardUrl": "https://testapp.bookonelocal.co.nz",
        "username": 'demoUserName',
        "userStatus": "NEW"
    }

    updateUser = requests.post(updateUserApi, json=updateUserdata)
    updateUserStatusCode = updateUser.status_code
    if updateUserStatusCode == 200:
        print('User data update api status code',updateUserStatusCode)
    
    return updateUserStatusCode

    
