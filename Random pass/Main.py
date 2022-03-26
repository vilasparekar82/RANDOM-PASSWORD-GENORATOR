import random
from random import randint


Password = ""
for i in range(10):
    i = chr(randint(65, 90))
    Password = str(Password) + i 
print(Password)