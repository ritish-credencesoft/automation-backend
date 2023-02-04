import requests
from variables import *
import helper

config=helper.read_config()

s=requests.Session()

def addSubscription(propertyId,userId,header):

    if env_variable == 'TEST':
        addSubscriptionApi=config['TestApi']['addsubscriptionapi'].replace('{propertyId}',str(propertyId))
    elif env_variable == 'PRODUCTION':
        addSubscriptionApi=config['ProductionApi']['addsubscriptionapi'].replace('{propertyId}',str(propertyId))

    suscriptionData = {
        "annualAmount": 0,
        "currency": "INR",
        "description": "",
        "discountAmount": 0,
        "id": userId,
        "imageUrl": "string",
        "monthlyAmount": 0,
        "name": "string",
        "organisationId": 1,
        "propertyId": propertyId,
        "specialNotes": "string",
        "subscriptionType": "MONTHLY"
    }

    addSubscriptionApiRes = s.post(
        addSubscriptionApi, headers=header, json=suscriptionData)
    subscriptionStatusCode = addSubscriptionApiRes.status_code
    if subscriptionStatusCode == 200:
        print('Subscription add api status code',subscriptionStatusCode)
    
    return subscriptionStatusCode
