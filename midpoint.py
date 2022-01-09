# Name: Johannes Schneemann
# Date: 1/8/2022
# Description: This is a simple program finds the midpoint

# set the midpoint
midpoint = 12

# make two empty lists
lower = []; upper = []

# split the numbers into lower and upper
for i in range(32):
    if (i < midpoint):
        lower.append(i)
    else:
        upper.append(i)
print("lower:", lower)
print("upper:", upper)
