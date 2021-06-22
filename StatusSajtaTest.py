import requests
import Konstante



def RadiLiSajt(BASE_URL):
    response= requests.get(BASE_URL,timeout=10)
    if (response.status_code==200):
        return True
    else:
        return False

if (RadiLiSajt(Konstante.BASE_URL)==True):
    print('Website je online')
else:
    print('Webiste nije online')





