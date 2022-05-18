import math

def get_factors(to_factor):
    if to_factor == 1:
        return [1]

    # Use (math. ) for  calculations for ciel of (x) and for square root

my_list = []
num_sqrt = math.ceil(math.sqrt(to_factor))

# +1 for expanding range
for num in range(1, num sqrt + 1):
    if to_factor % num == 0:

        # find factor by division, get whole number only
        a_factor = to_factor // num

        my_list.append(a_factor)
        my_list.append(num)

my_list.sort()

# Unique factor stored here
my_list = list(set(my_list))
return my_list