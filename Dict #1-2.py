a = {
     "r1" :  {"location":"21 New Globe Walk","vendor":"Cisco","model":"4451","ios":"15.4","ip":"10.255.0.1"},
     "r2" :  {"location":"21 New Globe Walk","vendor":"Cisco","model":"4451","ios":"15.4","ip":"10.255.0.2"},
     "sw1" : {"location":"21 New Globe Walk","vendor":"Cisco","model":"3850","ios":"3.6.XE","ip": "10.255.0.101","vlans":"10,20,30","routing":"True"}
    }
b=input('Введите название устройства: ')
c=input('Введите имя параметра: ')
d=a[b].pop(c)
print(b)
print(d)