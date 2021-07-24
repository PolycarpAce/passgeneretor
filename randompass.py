#import the necessary modules

import random
import string

print('Hi, Welcome to Password generator')

#length of Password
length = 8

#define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation 

#combine the data

all = lower + upper + num + symbols

#use random

temp = random.sample(all,length)

#create the Password
password = "".join(temp)

#print password

print(password)