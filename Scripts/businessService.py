import requests
from variables import *
import helper

config=helper.read_config()

s=requests.Session()

def businessServiceApi(propertyId,header):

    if env_variable == 'TEST':
        businessServiceApi=config['TestApi']['businessserviceapi']
    elif env_variable == 'PRODUCTION':
        businessServiceApi=config['ProductionApi']['businessserviceapi']

    businessServ={
        "fontAwesomeUrl":None,
        "name":"Accommodation",
        "description":None,
        "groupName":None,
        "code":"03",
        "organisationId":1,
        "businessTypeId":175,
        "bookingButtonLabelText":"Accommodation",
        "businessLocationName":"Accommodation",
        "businessProductName":"Accommodation",
        "businessServiceName":"Accommodation",
        "businessTermLocation":None,
        "businessTermResource":None,
        "canChangeBusinessAddress":None,
        "customerLocationName":"Accommodation",
        "provideBusinessAndCustomerAddress":None,
        "propertyId":propertyId
    }
    businessService = s.post(
                businessServiceApi, json=businessServ, headers=header)
    businessServiceStatusCode = businessService.status_code
    if businessServiceStatusCode == 200:
        print('businessService api status code',businessServiceStatusCode)
    
    return businessServiceStatusCode