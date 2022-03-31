import random

random_number = random.random()
if random_number < 0.25:
    print("try to go right")
elif random_number > 0.25 and random_number < 0.5:
    print("try to go left")
elif random_number > 0.5 and random_number < 0.75:
    print("try to go top")
else:
    print("try to go bottom")