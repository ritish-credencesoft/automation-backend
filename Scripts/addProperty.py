import json
import requests
from variables import *
import helper

config=helper.read_config()

s=requests.Session()

def addProperty(header,userId):

    propertyApiObj = {
        "name": businessName,
        "shortName": businessShortName,
        "email": businessEmail,
        "slogan": "Paradiso El Heaven",
        "landphone": "",
        "mobile": mobileNumber,
        "whatsApp": "",
        "managerFirstName": 'firstName',
        "managerLastName": 'lastName',
        "managerContactNo": managerContactNumber,
        "managerEmailAddress": businessEmail,
        "seoFriendlyName": seoName,
        "businessSubtype": "Hotels",
        "address": {
            "country": country,
            "postcode": postcode,
            "streetNumber": "",
            "streetName": streetName,
            "suburb": suburb,
            "city": city,
            "state": state,
            "locality": suburb,
            "addressLine1": None,
            "addressLine2": None
        },
        "verified": True,
        "propertyStatus": "COMPLETED",
        "gstNumber": "asd12345",
        "vatNumber": "skm01",
        "udyamRegistrationNumber": "12034",
        "pricePerNight": 900,
        "pricePerWeek": 6300,
        "priceFortNight": 13500,
        "priceMonthly": 27000,
        "minimumOccupancy": 1,
        "maximumOccupancy": 18,
        "logoUrl": "https://bookonelocal.in/cdn/2021-05-25-040216327-h.jpg",
        "localCurrency": "INR",
        "placeId": googlePlaceId,
        "website": "https://bookonelocal.in",
        "paymentGateway": "atom",
        "paymentGatewayApiKey": "dId9ckHoLHhmGyUp",
        "paymentGatewayPublicKey": "CKtrgR16394366122554",
        "paymentGatewayCallbackUrl": "https://testapi.bookonelocal.co.nz/api-bookone/api/website/paytmResponse/",
        "organisationId": 1,
        "longitude": longitude,
        "latitude": latitude,
        "businessType": businessType,
        "businessDescription": "<p>Welcome to our property.<br>&nbsp;</p>",
        "plan": "Business Premium",
        "facebook": "",
        "instagram": "bookstartest",
        "videoLink": "https://www.youtube.com/embed/vUnCpQdwPVI",
        "imageList": [
            {
                "description": "Test image",
                "id": str(userId),
                "mainImage": True,
                "name": "string",
                "url": 'https://bookonelocal.in/cdn/2021-02-03-104317314-bi1.jpg'
            }
        ],
        "taxDetails": [
        {
        "name": "CGST",
        "percentage": 6,
        "country": country,
        "state": state,
        "taxableAmount": 1999,
        "taxAmount": 119.94,
        "taxSlabsList": [
            {
            "minAmount": 1,
            "maxAmount": 1000,
            "percentage": 0
            },
            {
            "minAmount": 1001,
            "maxAmount": 7500,
            "percentage": 6
            },
            {
            "minAmount": 7501,
            "maxAmount": 1000000000,
            "percentage": 9
            }
        ]
        },
        {
        "name": "IGST",
        "percentage": 6,
        "country": country,
        "state": state,
        "taxableAmount": 1999,
        "taxAmount": 119.94,
        "taxSlabsList": [
            {
            "minAmount": 0,
            "maxAmount": 1000,
            "percentage": 0
            },
            {
            "minAmount": 1001,
            "maxAmount": 7500,
            "percentage": 6
            },
            {
            "minAmount": 7501,
            "maxAmount": 1000000000,
            "percentage": 9
            }
        ]
        },
        {
        "name": "SGST",
        "percentage": 6,
        "country": country,
        "state": state,
        "taxableAmount": 1999,
        "taxAmount": 119.94,
        "taxSlabsList": [
            {
            "minAmount": 0,
            "maxAmount": 1000,
            "percentage": 0
            },
            {
            "minAmount": 1001,
            "maxAmount": 7500,
            "percentage": 6
            },
            {
            "minAmount": 7501,
            "maxAmount": 1000000000,
            "percentage": 9
            }
        ]
        },
        {
        "name": "GST",
        "percentage": 12,
        "country":country ,
        "state":state ,
        "taxableAmount": 1999,
        "taxAmount": 239.88,
        "taxSlabsList": [
            {
            "minAmount": 0,
            "maxAmount": 1000,
            "percentage": 0
            },
            {
            "minAmount": 1001,
            "maxAmount": 7500,
            "percentage": 12
            },
            {
            "minAmount": 7501,
            "maxAmount": 1000000000,
            "percentage": 18
            }
        ]
        }
    ],
    }

    if env_variable == 'TEST':
        addPropertyApi=config['TestApi']['addpropertyapi']
    elif env_variable == 'PRODUCTION':
        addPropertyApi=config['ProductionApi']['addpropertyapi']

    addPropertyRes = s.post(
        addPropertyApi, json=propertyApiObj, headers=header)

    propertyInfo = json.loads(addPropertyRes.content)
    propertyId = propertyInfo['id']
    addPropertyStatusCode = addPropertyRes.status_code
    if addPropertyStatusCode == 200:
        print('Add property api status code ', addPropertyStatusCode)

    p={
        'propertyId':propertyId,
        'status':addPropertyStatusCode
    }

    return p

    
