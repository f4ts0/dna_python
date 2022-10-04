from Api_python import get_devices

devices = get_devices()

for i in devices: #["response"]:# ako pogledas ceo response (ili iz postmana) videces da je response na api u stvari
                                # dictionary sa vrednosti "response" : lista vrednosti
                                # #Nama u sustini treba lista vrednosti pa omitujemo "response" ovde. 
                                # #Moezemo i u main modulu da omitujemo. Omit je ["response"]
                                # preferiram da to uradimo u main programu
    
    
    print ("Device: ",i["type"], "|", "Serijski Broj: ",i["serialNumber"],"|","IP adresa: ", i["managementIpAddress"])

#opcija 2

import Api_python

devices1 = Api_python.get_devices()

for i in  devices1:
    print ("Device: ",i["type"], "|", "Serijski Broj: ",i["serialNumber"],"|","IP adresa: ", i["managementIpAddress"])