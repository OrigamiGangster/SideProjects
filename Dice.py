import math
import random

def random_pi():
    return math.ceil(random.randint(1,6)) 

for _ in range(2):
    print(random_pi())