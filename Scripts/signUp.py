import requests
import helper
from variables import env_variable

config=helper.read_config()

s=requests.Session()

def signUp(businessEmail,password):

    if env_variable == 'TEST':
        signupApi=config['TestApi']['signupapi']
    elif env_variable == 'PRODUCTION':
        signupApi=config['ProductionApi']['signupapi']

    userSingUpdata = {
        "email": businessEmail,
        "password": password,
        "confirmPassword": password
    }
    p = s.post(signupApi, json=userSingUpdata)
    signUpStatusCode = p.status_code
    
    return signUpStatusCode