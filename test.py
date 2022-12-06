import random


characters = list('abcdefghijklmnopqrstuvwxyz')
length = 10

the_password = ''.join(random.choice(characters) for _ in range(length))

print(the_password)
