import requests
import hashlib
import sys
import pdb

def request_api_data(query_char):
    url='https://api.pwnedpasswords.com/range/'+query_char
    res= requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'error fetching:{res.status_code}')
    return res

def pwned_api_check(password):
     sha1password=hashlib.sha1(password.encode('utf-8'))
     passw=sha1password.hexdigest().upper()
     first5char, tail=passw[:5],passw[5:]
     res=request_api_data(first5char)

     return get_password_leaks_count(res,tail)


def get_password_leaks_count(hashes, hash_to_check):
     hashes=(line.split(':') for  line in   hashes.text.splitlines())
     for h, count in hashes:
         if h==hash_to_check:
             return count
     return 0    


def main(args):
     for password in args:
         count=pwned_api_check(password)
         if count:
             print(f'{password} was found {count} times, please change your password, it is not secure')
         else:
             print(f'{password} was not found, use can use your password without any security issue')

     return 'done!'       




if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))