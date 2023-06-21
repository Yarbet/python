set_countries = {'col', 'mex', 'bol'}

size = len(set_countries)
print(size)

print('col' in set_countries)
print('per' in set_countries)

#add
set_countries.add('pe')
print(set_countries)

#update
set_countries.update({'ar', 'cl'})
print(set_countries)

#remove
set_countries.remove('cl')
print(set_countries)

#set_countries.remove('arg')
set_countries.discard('arg')
print(set_countries)

#limpiar
set_countries.clear()
print(set_countries)
print(len(set_countries))

#random
set_countries.pop('bol')
print(set_countries)