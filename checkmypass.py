import requests
import hashlib

def request_api_data(query_char):
    url='https://api.pwnedpasswords.com/rang/'+query_char
    res= request.get(url)
    if res.status.code != 200:
        raise RuntimeError(f'error fetching:{res.status.code}')
    return res

 def pwned_api_check(password):
     sha1password=hashlib.sha1(password.encode('utf-8'))
     passw=sha1password.hexdigest().upper()
     first5char, tail=passw[:5],passw[5:]
     res=request_api_data(first5char)


def read_res(response)   
