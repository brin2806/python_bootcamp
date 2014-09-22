birthdays = dict([('Luke Skywalker', '5/4/19'), ('obi-wan kenobi', '3/11/57'), ('Darth Vader', '4/1/41')])
#print(birthdays)


if 'yoda' in birthdays:
    birthdays['yoda']
else:
    birthdays['yoda'] = 'unknown'
#print(birthdays)        

if 'Darth Vader' in birthdays:
    birthdays['Darth Vader']
else:
    birthdays['Darth Vader'] = 'unknown'
#print(birthdays)   


#for name in birthdays:
 #   print(name, birthdays[name])

del (birthdays['Darth Vader'])
print(birthdays)