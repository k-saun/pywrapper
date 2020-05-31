import sys
sys.path.append("/Users/keegansaunders/Documents/HP/cs_to_py/pyCalc/pythonnet-2.4.0/")
import clr
clr.AddReference("/Users/keegansaunders/Documents/HP/cs_to_py/DynamicCS/library/bin/Debug/netstandard2.0/library.dll")

from library import DynamicCalc
calc=DynamicCalc()
 
print(calc.__class__.__name__)
# display the name of the class: 'DynamicCalc' python3 -m pip install -U pythonnet --user
 
a=7.5
b=2.5
 
res = calc.add(a, b)
print(a, '+', b, '=', res)
 
res = calc.sub(a, b)
print (a, '-', b, '=', res)
 
input('Press any key to finish...')