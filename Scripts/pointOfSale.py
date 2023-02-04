import requests
from variables import *
import helper

config=helper.read_config()

s=requests.Session()

def pointOfSaleApi(propertyId,header):

    if env_variable == 'TEST':
        pointOfSaleApi=config['TestApi']['pointofsaleapi'].replace('{propertyId}',str(propertyId))
    elif env_variable == 'PRODUCTION':
        pointOfSaleApi=config['ProductionApi']['pointofsaleapi'].replace('{propertyId}',str(propertyId))

    pointOfSalePayload={
                        "propertyId": propertyId,
                        "counterName": "counter 1",
                        "counterNumber": "1",
                        "operatorName": [
                            "Operator1"
                        ]
                        }
    pointOfSale=s.post(
                pointOfSaleApi, json=pointOfSalePayload, headers=header)
    pointOfSaleStatusCode=pointOfSale.status_code
    if pointOfSaleStatusCode == 200:
        print('pointOfSale Api Status Code',pointOfSaleStatusCode)
    
    return None