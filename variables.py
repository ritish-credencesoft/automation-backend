import json,sys
sys.path.append('\\'.join(sys.path[0].split('\\')[:-1]))

f = open(r'Data/test3.json')
jsonData = json.load(f)



env_variable='TEST'


for item in jsonData:
    # JSON READ
    businessName = item['BusinessName']
    businessShortName = ''
    password = 'Pass@1234'
    businessShortNameSplit = businessName.split()
    for i in businessShortNameSplit:
        businessShortName = businessShortName+i[0]

    seoFriendlyName = businessName.split()
    seoName = '-'.join(seoFriendlyName)

    businessUrl = item['BusinessUrl']
    city = item['city']
    country = item['country']
    postcode = item['postcode']
    state = item['state']
    streetName = item['streetName']
    suburb = item['subUrb']
    businessType = item['BusinessType']
    collectedBy = item['dataCollectedBy']
    businessEmail = item['email']
    managerContactNumber = item['managerContactNo'].strip()
    mobileNumber = item['mobile'].strip()
    businessSource = item['source']
    businessStatus = item['status']
    roomType = item['Room Type']
    roomPlan = item['Room Plan']
    longitude = item['Longitude']
    latitude = item['Latitude']
    googlePlaceId = item['Google place id']
    try:
        website = item['website']
    except:
        website = ''
    status = item['status']
    source = item['source']
    try:
        images = item['images']
    except:
        images=[]


