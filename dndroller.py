#!/usr/bin/env python3

import random

# Get user input
num_d20 = input('Enter number of d20: ')
num_d12 = input('Enter number of d12: ')
num_d10 = input('Enter number of d10: ')
num_d8 = input('Enter number of d8: ')
num_d6 = input('Enter number of d6: ')
num_d4 = input('Enter number of d4: ')
modifier = input('Enter bonus: ')

# Roll the dice
d20 = random.randint(1,20)
d12 = random.randint(1,12)
d10 = random.randint(1,10)
d8 = random.randint(1,8)
d6 = random.randint(1,6)
d4 = random.randint(1,4)

# Figure out the total
total = (num_d20*d20)+(num_d12*d12)+(num_d10*d10)+(num_d8*d8)+(num_d6*d6)+(num_d4*d4)+modifier

print("You rolled ", num_d20, "d20 + ", num_d12, "d12 + ", num_d10, "d10 + ", num_d8, "d8 + ", num_d6, "d6 + ", num_d4, "d4 + ", modifier)
print("Your final roll was ", total, ".")
