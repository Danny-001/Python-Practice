#Importing modules in Python  allows you to use code (functions, classes, variables, etc.) written in other files or libraries in your program

import sys

print(sys.version)

#importing sprcific items from a module

from datetime import datetime

print(datetime.now())

#importing with an alias

from datetime import datetime as dt

print(dt.now())

from math import sqrt as srt

print(srt(49))
print(srt(64))
print(srt(81))


from math import pi as p
print(p)
print(p*p)  
print(p*p*p)
print(p*p*p*p)


from math import e as euler
print(euler)
print(euler*euler)
print(euler*euler*euler)
print(euler*euler*euler*euler)


from math import factorial as f
print(f(5))
print(f(6))
print(f(7))