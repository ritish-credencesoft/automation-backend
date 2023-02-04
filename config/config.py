# TBD :
'''

The main purpose of this script is to select the config file either for test or prod as per the requirement.

'''

import configparser

config_file=configparser.ConfigParser()

config_file.add_section('TestApi')

config_file.set('TestApi','signUpApi','https://testapi.bookonelocal.co.nz/api-bookone/api/user/signup')
config_file.set('TestApi','loginApi','https://testapi.bookonelocal.co.nz/api-bookone/api/user/login')
config_file.set('TestApi','updateUserApi','https://testapi.bookonelocal.co.nz/api-bookone/api/user/updateUser')
config_file.set('TestApi','addPropertyApi','https://testapi.bookonelocal.co.nz/api-bookone/api/property/user/add/property')
config_file.set('TestApi','addSubscriptionApi','https://testapi.bookonelocal.co.nz/api-bookone/api/property/{propertyId}/addSubscription')
config_file.set('TestApi','addRoomApi','https://testapi.bookonelocal.co.nz/api-bookone/api/property/{propertyId}/user/add/room')
config_file.set('TestApi','getRoomDetailsApi','https://testapi.bookonelocal.co.nz/api-bookone/api/property/{propertyId}/rooms')
config_file.set('TestApi','addRoomPlanApi','https://testapi.bookonelocal.co.nz/api-bookone/api/room/property/{propertyId}/room/{individualRoomId}/roomPlan')
config_file.set('TestApi','yearlyGenerateRatesApi','https://testapi.bookonelocal.co.nz/api-bookone/api/property/addYearlyRates')
config_file.set('TestApi','pointOfSaleApi','https://testapi.bookonelocal.co.nz/api-bookone/api/property/{propertyId}/pointOfSale')
config_file.set('TestApi','businessServiceApi','https://testapi.bookonelocal.co.nz/api-bookone/api/businessService')
config_file.set('TestApi','addAvailabilityByDate','https://testapi.bookonelocal.co.nz/api-bookone/api/availability/addAvailabilityByRoomAndDateRange')
config_file.set('TestApi','addOrUpdatePlanApi','https://testapi.bookonelocal.co.nz/api-bookone/api/availability/addOrUpdatePlan')

config_file.add_section('ProductionApi')

config_file.set('ProductionApi','signUpApi','https://api.bookonelocal.in/api-bookone/api/user/signup')
config_file.set('ProductionApi','loginApi','https://api.bookonelocal.in/api-bookone/api/user/login')
config_file.set('ProductionApi','updateUserApi','https://api.bookonelocal.in/api-bookone/api/user/updateUser')
config_file.set('ProductionApi','addPropertyApi','https://api.bookonelocal.in/api-bookone/api/property/user/add/property')
config_file.set('ProductionApi','addSubscriptionApi','https://api.bookonelocal.in/api-bookone/api/property/{propertyId}/addSubscription')
config_file.set('ProductionApi','addRoomApi','https://api.bookonelocal.in/api-bookone/api/property/{propertyId}/user/add/room')
config_file.set('ProductionApi','getRoomDetailsApi','https://api.bookonelocal.in/api-bookone/api/property/{propertyId}/rooms')
config_file.set('ProductionApi','addRoomPlanApi','https://api.bookonelocal.in/api-bookone/api/room/property/{propertyId}/room/{individualRoomId}/roomPlan')
config_file.set('ProductionApi','yearlyGenerateRatesApi','https://api.bookonelocal.in/api-bookone/api/property/addYearlyRates')
config_file.set('ProductionApi','pointOfSaleApi','https://api.bookonelocal.in/api-bookone/api/property/{propertyId}/pointOfSale')
config_file.set('ProductionApi','businessServiceApi','https://api.bookonelocal.in/api-bookone/api/businessService')
config_file.set('ProductionApi','addAvailabilityByDate','https://api.bookonelocal.in/api-bookone/api/availability/addAvailabilityByRoomAndDateRange')
config_file.set('ProductionApi','addOrUpdatePlanApi','https://api.bookonelocal.in/api-bookone/api/availability/addOrUpdatePlan')



with open(r"configurations.ini", 'w') as configfileObj:
    config_file.write(configfileObj)
    configfileObj.flush()
    configfileObj.close()
