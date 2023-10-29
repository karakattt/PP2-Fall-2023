
import json


with open('E:\SUBJECT-My study))\III-SEMESTER\PP2\labs\lab6\json\sample-data.json', 'r') as file:
    data=json.load(file)

imdata=data.get('imdata', [])


print("Interface Status \n", '='*80)
# print("DN                                                 Description           Speed    MTU  ")
print("{:<50} {:<20} {:<10} {:<10}".format("DN", "Description", "Speed", "MTU"))
print('-'*80)

for item in imdata:
    l1PhysIf=item.get('l1PhysIf', {})
    attributes=l1PhysIf.get('attributes', {})
    dn=attributes.get('dn', '')
    description=attributes.get('descr', '')
    speed=attributes.get('speed', '')
    mtu=attributes.get('mtu', '')

    print("{:<50} {:<20} {:<10} {:<10}".format(dn, description, speed, mtu))

file.close()



