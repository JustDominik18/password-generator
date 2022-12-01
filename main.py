import random
import string

print('Ahoj, Vítej v Generátoru hesel (By Dominik)')

length = int(input('\nZadejte délku hesla: '))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num

temp = random.sample(all,length)

password = "".join(temp)

print(password)