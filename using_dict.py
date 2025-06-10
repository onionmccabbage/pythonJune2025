# e may import an entire library
# import datetime
import time
# or we may just import the modules we need from that library
from datetime import datetime

now = datetime.date( datetime.today() )
print(now)
#since we imported the entire time library we must specify time.time()
print(time.time())

# there is a data type known as dictionary or 'dict'
# dict is a non-ordinal mutable collection of key:value pairs (of any data type)
# NB id is one of the few things you do not have to put in quotes
equip = {id:3452, 'date':now, 'qos':80, 'freq':(433, 866)}
# we may add or mutate members of the dict
equip['qos'] = 90 # mutate this member
equip['latlon'] = (0, 52)


print(equip, type(equip))

# we may iterate the contents of a dict like this
for (k, v) in equip.items():
    print(f'value of {k} is {v}')
