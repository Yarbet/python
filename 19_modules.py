import sys
print(sys.path)

import re
text = 'Mi numero de teléfono es 959219119, el codigo del pais es 51, mi numero de la suerte es 69'
result = re.findall('[0-9]+', text)
print(result)

import time 

timestamp = time.time()
print(timestamp)

local = time.localtime()
result = time.asctime(local)
print(result)

import collections

numbers = [1,2,3,4,5,2,1,2,4,2,5]
counter = collections.Counter(numbers)
print(counter)
