import requests
from variables import *
import helper

config=helper.read_config()

s=requests.Session()

def yearlyGenerateApi(propertyId,header):

    if env_variable == 'TEST':
        yearlyRatesApi=config['TestApi']['yearlygenerateratesapi']
    elif env_variable == 'PRODUCTION':
        yearlyRatesApi=config['ProductionApi']['yearlygenerateratesapi']

    yearlyRatesPayload={
    "id": propertyId,
    "name": "ROSHAN",
    "shortName": businessShortName,
    "email": businessEmail,
    "slogan": "Paradiso El Heaven",
    "landphone": "",
    "mobile": mobileNumber,
    "whatsApp": "",
    "managerFirstName": "roshan",
    "managerLastName": "mishra",
    "managerContactNo": mobileNumber,
    "managerEmailAddress": businessEmail,
    "address": {
        "country": country,
        "postcode": postcode,
        "streetNumber":'' ,
        "streetName": streetName,
        "suburb": suburb,
        "city": city,
        "state": state,
        "locality": "belpur-jn",
        "addressLine1": None,
        "addressLine2": None
    },
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
    "noOfFloor": 6,
    "noOfRoomType": 3,
    "numberOfRooms": 9,
    "website": "https://bookonelocal.in",
    "paymentGateway": "atom",
    "paymentGatewayApiKey": "dId9ckHoLHhmGyUp",
    "paymentGatewayPublicKey": "CKtrgR16394366122554",
    "paymentGatewayCallbackUrl": "https://testapi.bookonelocal.co.nz/api-bookone/api/website/paytmResponse/",
    "organisationId": 1,
    "longitude": longitude,
    "latitude": latitude,
    "businessType": "Accommodation",
    "businessDescription": "<p>Welcome to our property.<br>&nbsp;</p>",
    "plan": "Business Premium",
    "facebook": "qwe",
    "instagram": "bookstartest",
    "videoLink": "https://www.youtube.com/embed/vUnCpQdwPVI",
    "bankAccount": {
        "bankName": "Standard Bank",
        "branchName": "North Odisha",
        "accountName": "BookStarTest",
        "accountNumber": "GGYUGy123213",
        "swiftCode": "559"
    },
    "mobileWallet": {
        "firstName": "Book1",
        "lastName": "Test1",
        "phoneNumber": "+91864684883",
        "walletProvider": "PayTM",
        "walletUrl": "",
        "qrCode": None
    },
    "subscriptionList": [],
    "verified": True,
    "seoFriendlyName": "Book-Star-Test",
    "imageList": [
        {
        "id": None,
        "name": "file",
        "url": "https://bookonelocal.in/cdn/2021-02-03-104317314-bi1.jpg",
        "description": None,
        "mainImage": False
        },
        {
        "id": None,
        "name": "file",
        "url": "https://bookonelocal.in/cdn/2021-02-03-104321894-5b947f54-ee5b-4eec-9df9-afda183ae758.jpg",
        "description": None,
        "mainImage": False
        },
        {
        "id": None,
        "name": "file",
        "url": "https://bookonelocal.in/cdn/2021-02-03-104326649-hs1.jpeg",
        "description": None,
        "mainImage": False
        },
        {
        "id": None,
        "name": "file",
        "url": "https://bookonelocal.in/cdn/2021-02-03-104330311-90cd2ec7-1b22-4706-b757-aca870897ce0.jpg",
        "description": None,
        "mainImage": False
        },
        {
        "id": None,
        "name": "file",
        "url": "https://bookonelocal.in/cdn/2021-07-09-103900232-world-cuisine.jpg",
        "description": None,
        "mainImage": False
        },
        {
        "id": None,
        "name": "file",
        "url": "https://blbl.co.nz/cdn/2022-03-04-112458938-34bcca9e-5210-4722-b207-326d223184df.jpeg",
        "description": None,
        "mainImage": False
        },
        {
        "id": None,
        "name": "file",
        "url": "https://blbl.co.nz/cdn/2022-03-04-112507316-8fa66952-e2fc-4300-a7bf-0d4ec3e7d4dd.jpeg",
        "description": None,
        "mainImage": False
        },
        {
        "id": None,
        "name": "file",
        "url": "https://blbl.co.nz/cdn/2022-03-04-112513661-6a8f6078-8e48-4999-a080-dc703f5a2153.jpeg",
        "description": None,
        "mainImage": False
        },
        {
        "id": None,
        "name": "file",
        "url": "https://blbl.co.nz/cdn/2022-03-04-112520035-4fc8f4e1-3736-4d8e-9bf8-a13689150ef1.jpeg",
        "description": None,
        "mainImage": False
        },
        {
        "id": None,
        "name": "file",
        "url": "https://blbl.co.nz/cdn/2022-03-04-112615489-banani dental 3.jpg",
        "description": None,
        "mainImage": False
        },
        {
        "id": None,
        "name": "file",
        "url": "https://blbl.co.nz/cdn/2022-03-04-112620670-banani dental 2.jpg",
        "description": None,
        "mainImage": False
        },
        {
        "id": None,
        "name": "file",
        "url": "https://blbl.co.nz/cdn/2022-03-04-112627158-banani dental 1.jpg",
        "description": None,
        "mainImage": False
        },
        {
        "id": None,
        "name": "file",
        "url": "https://blbl.co.nz/cdn/2022-03-04-112630891-276126767.jpg",
        "description": None,
        "mainImage": False
        },
        {
        "id": None,
        "name": "file",
        "url": "https://blbl.co.nz/cdn/2022-03-04-112634988-276126731.jpg",
        "description": None,
        "mainImage": False
        },
        {
        "id": None,
        "name": "file",
        "url": "https://blbl.co.nz/cdn/2022-03-04-112638819-275471139.jpg",
        "description": None,
        "mainImage": False
        },
        {
        "id": None,
        "name": "file",
        "url": "https://blbl.co.nz/cdn/2022-03-04-112643535-275471137.jpg",
        "description": None,
        "mainImage": False
        },
        {
        "id": None,
        "name": "file",
        "url": "https://blbl.co.nz/cdn/2022-03-04-112647444-275471135.jpg",
        "description": None,
        "mainImage": False
        },
        {
        "id": None,
        "name": "file",
        "url": "https://blbl.co.nz/cdn/2022-03-04-112653367-275471132.jpg",
        "description": None,
        "mainImage": False
        },
    ],
    
    "socialMediaLinks": [
        "bookstartest@koo.in"
    ],
    "detailedView": {
        "yearWiseVisits": {
        "2021": {
            "MAY": 24,
            "JULY": 127,
            "JUNE": 136,
            "APRIL": 45,
            "MARCH": 134,
            "AUGUST": 38,
            "JANUARY": 59,
            "OCTOBER": 57,
            "DECEMBER": 414,
            "FEBRUARY": 138,
            "NOVEMBER": 24,
            "SEPTEMBER": 30
        },
        "2022": {
            "MAY": 923,
            "JULY": 303,
            "JUNE": 758,
            "APRIL": 1003,
            "MARCH": 307,
            "JANUARY": 47,
            "OCTOBER": 543,
            "DECEMBER": 537,
            "NOVEMBER": 2385,
            "SEPTEMBER": 27
        }
        },
        "totalNumberOfVisits": 8059
    },
    "noOfBookOneReview": 5,
    "bookOneRating": 4.2,
    "sacCode": "98744",
    "fssaiRegNumber": "234234234",
    "businessSubtype": "Hotels",
    "propertyServicesList": [
        {
        "id": 1000,
        "organisationId": 1,
        "name": "Adult Meal",
        "description": None,
        "logoUrl": "https://bookonelocal.in/cdn/2021-06-09-120141269-u4.png",
        "imageUrl": "https://bookonelocal.in/cdn/2021-06-09-120145330-u4.png",
        "businessType": businessType,
        "serviceType": "Breakfast",
        "afterTaxAmount": 250,
        "beforeTaxAmount": 238.0952380952381,
        "taxAmount": 11.904761904761903,
        "taxPercentage": 5,
        "servicePrice": 238.0952380952381,
        "applicableToChild": True,
        "applicableToAdult": True
        },
        {
        "id": 1001,
        "organisationId": 1,
        "name": "Lunch",
        "description": None,
        "logoUrl": "https://bookonelocal.in/cdn/2021-06-09-122528713-2.png",
        "imageUrl": "https://bookonelocal.in/cdn/2021-06-09-122531337-2.png",
        "businessType": businessType,
        "serviceType": "Lunch",
        "afterTaxAmount": 267.8,
        "beforeTaxAmount": 260,
        "taxAmount": 7.8,
        "taxPercentage": 3,
        "servicePrice": 260,
        "applicableToChild": True,
        "applicableToAdult": True
        },
        {
        "id": 1002,
        "organisationId": 1,
        "name": "Dinner",
        "description": None,
        "logoUrl": "https://bookonelocal.in/cdn/2021-06-09-122555495-4.jpg",
        "imageUrl": "https://bookonelocal.in/cdn/2021-06-09-122558283-4.jpg",
        "businessType": businessType,
        "serviceType": "Dinner",
        "afterTaxAmount": 525,
        "beforeTaxAmount": 500,
        "taxAmount": 25,
        "taxPercentage": 5,
        "servicePrice": 500,
        "applicableToChild": False,
        "applicableToAdult": False
        },
        {
        "id": 1003,
        "organisationId": 1,
        "name": "Tea-Coffee",
        "description": None,
        "logoUrl": "https://bookonelocal.in/cdn/2021-06-09-122612213-5.jpg",
        "imageUrl": "https://bookonelocal.in/cdn/2021-06-09-122615244-5.jpg",
        "businessType": businessType,
        "serviceType": "Tea-Coffee",
        "afterTaxAmount": 106.05,
        "beforeTaxAmount": 101,
        "taxAmount": 5.05,
        "taxPercentage": 5,
        "servicePrice": 101,
        "applicableToChild": False,
        "applicableToAdult": True
        },
        {
        "id": 1004,
        "organisationId": 1,
        "name": "Laundry",
        "description": None,
        "logoUrl": "https://bookonelocal.in/cdn/2021-06-09-122625875-u2.png",
        "imageUrl": "https://bookonelocal.in/cdn/2021-06-09-122631517-u2.png",
        "businessType": businessType,
        "serviceType": "Laundry",
        "afterTaxAmount": 153,
        "beforeTaxAmount": 150,
        "taxAmount": 3,
        "taxPercentage": 2,
        "servicePrice": 150,
        "applicableToChild": True,
        "applicableToAdult": False
        },
        {
        "id": 1005,
        "organisationId": 1,
        "name": "Late Check-Out",
        "description": None,
        "logoUrl": "https://bookonelocal.in/cdn/2021-06-09-122643445-u1.png",
        "imageUrl": "https://bookonelocal.in/cdn/2021-06-09-122647337-u1.png",
        "businessType": businessType,
        "serviceType": "Late Check-Out",
        "afterTaxAmount": 50,
        "beforeTaxAmount": 50,
        "taxAmount": 0,
        "taxPercentage": None,
        "servicePrice": None,
        "applicableToChild": False,
        "applicableToAdult": False
        },
        {
        "id": 1006,
        "organisationId": 1,
        "name": "Pick Up",
        "description": None,
        "logoUrl": "https://bookonelocal.in/cdn/2021-06-09-124125378-8.png",
        "imageUrl": "https://bookonelocal.in/cdn/2021-06-09-124127900-8.png",
        "businessType": businessType,
        "serviceType": "Pick Up",
        "afterTaxAmount": None,
        "beforeTaxAmount": None,
        "taxAmount": None,
        "taxPercentage": None,
        "servicePrice": None,
        "applicableToChild": False,
        "applicableToAdult": False
        },
        {
        "id": 1007,
        "organisationId": 1,
        "name": "Drop Off",
        "description": None,
        "logoUrl": "https://bookonelocal.in/cdn/2021-06-09-124140636-7.png",
        "imageUrl": "https://bookonelocal.in/cdn/2021-06-09-124143695-7.png",
        "businessType": businessType,
        "serviceType": "Drop Off",
        "afterTaxAmount": None,
        "beforeTaxAmount": None,
        "taxAmount": None,
        "taxPercentage": None,
        "servicePrice": None,
        "applicableToChild": False,
        "applicableToAdult": False
        },
        {
        "id": 1008,
        "organisationId": 1,
        "name": "Transport Rent",
        "description": None,
        "logoUrl": "https://bookonelocal.in/cdn/2021-06-09-124157234-9.png",
        "imageUrl": "https://bookonelocal.in/cdn/2021-06-09-124159738-9.png",
        "businessType": businessType,
        "serviceType": "Transport Rent",
        "afterTaxAmount": None,
        "beforeTaxAmount": None,
        "taxAmount": None,
        "taxPercentage": None,
        "servicePrice": None,
        "applicableToChild": False,
        "applicableToAdult": False
        },
        {
        "id": 1010,
        "organisationId": 1,
        "name": "Extra Bed",
        "description": None,
        "logoUrl": None,
        "imageUrl": None,
        "businessType": businessType,
        "serviceType": "Extra Bed",
        "afterTaxAmount": None,
        "beforeTaxAmount": None,
        "taxAmount": None,
        "taxPercentage": None,
        "servicePrice": None,
        "applicableToChild": False,
        "applicableToAdult": False
        },
        {
        "id": None,
        "organisationId": 1,
        "name": "Airport Drop",
        "description": None,
        "logoUrl": None,
        "imageUrl": None,
        "businessType": businessType,
        "serviceType": "Transportation",
        "afterTaxAmount": None,
        "beforeTaxAmount": None,
        "taxAmount": None,
        "taxPercentage": None,
        "servicePrice": None,
        "applicableToChild": False,
        "applicableToAdult": False
        },
        {
        "id": None,
        "organisationId": 1,
        "name": "Child Food Charges ",
        "description": None,
        "logoUrl": None,
        "imageUrl": None,
        "businessType": businessType,
        "serviceType": "(Day Outing Picnic)",
        "afterTaxAmount": None,
        "beforeTaxAmount": None,
        "taxAmount": None,
        "taxPercentage": None,
        "servicePrice": None,
        "applicableToChild": False,
        "applicableToAdult": False
        },
        {
        "id": None,
        "organisationId": 1,
        "name": "Adult Food Charges ",
        "description": None,
        "logoUrl": None,
        "imageUrl": None,
        "businessType": businessType,
        "serviceType": " (Day Outing)",
        "afterTaxAmount": 997.5,
        "beforeTaxAmount": 950,
        "taxAmount": 47.5,
        "taxPercentage": 5,
        "servicePrice": 950,
        "applicableToChild": False,
        "applicableToAdult": False
        },
        {
        "id": None,
        "organisationId": 1,
        "name": "Wine",
        "description": None,
        "logoUrl": None,
        "imageUrl": None,
        "businessType": businessType,
        "serviceType": "Alcoholic",
        "afterTaxAmount": None,
        "beforeTaxAmount": None,
        "taxAmount": None,
        "taxPercentage": None,
        "servicePrice": None,
        "applicableToChild": False,
        "applicableToAdult": False
        }
    ],
    "nearbyAttractions": [],
    "propertyInvoicePrintHeader": True,
    "primaryColor": "#d82e1a",
    "secondaryColor": "#877dbb",
    "tertiaryColor": "#ed9633",
    "featuredBusiness": False
    }

    generateYearlyRates=s.post(yearlyRatesApi,json=yearlyRatesPayload,headers=header)
    yearlyStatusCode=generateYearlyRates.status_code
    if yearlyStatusCode == 200:
        print('Generate yearly rates status code ',generateYearlyRates.status_code)

    return yearlyStatusCode