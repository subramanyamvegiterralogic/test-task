from modules_ler import module1 as module
import time,  sys, os
from imp import reload
time.sleep(1)
x,y,z,a,b,c = 1,2,3,4,5,None
# reload(module)
# time.sleep(10)
# reload(module)
# time.sleep(10)
# reload(module)
# time.sleep(10)
print('Reload Module Testing')
print(dir())
# print(dir(module))
print(__name__)