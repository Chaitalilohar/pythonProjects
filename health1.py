import random

health = 70

difficulty = 2

potion_health = int(random.randint(24,100)/ difficulty)

health = health + potion_health

print(health)

#Output 
#112