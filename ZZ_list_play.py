import random

# set up a list
my_list = []

# Generate 4 random numbers between 1 and 10...
for item in range(0,4):

    # Generate random number between 1 and 10
    random_num = random.randint(1,10)

    # Add number to list
    my_list.append(random_num)

# Print the *unsorted* list...
print(my_list)

# Sort the list
my_list.sort()
my_list_len = len(my_list)

# Print the sorted list
print()
print(my_list)
print("The list has {} items".format(my_list_len))
print()