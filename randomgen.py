#import the necessary modules

import random
import string

print('Hi, Welcome to Password generator')

#length of Password
length = 8

all = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.sample(all,length))

print(password)