# -*- coding: utf-8 -*-
#!/usr/bin/python

import routeros_api
from random import randint
from datetime import datetime, date
# zdroj https://github.com/socialwifi/RouterOS-api/blob/master/README.md

connection = routeros_api.RouterOsApiPool('79.142.145.8', username='sspu', password='sspusspu', port=8902, plaintext_login=True )
api = connection.get_api()

# vypsani aktualniho adresslistu
list_queues = api.get_resource('/ip/firewall/address-list')
#print(list_queues.get())




#smazani adresy
for i in range(0,300):
    print(i)
    idToDelete = list_queues.get()[i]['id']
    print(i)
    print(i)
    print(idToDelete)
    list_queues.remove(id=idToDelete)


# otestovat rychlost zápisu cca 10K ip adress
# mazání přes ID - otestovat 10K
# Otestovat rychlost výpisu 10k záznamů



connection.disconnect()
