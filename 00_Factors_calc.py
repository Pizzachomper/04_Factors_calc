# Function go here

import math
# Puts series of symbols at the start and end of text
def statement_generator(text, decoration):

    # Make string with five charecters
    ends = decoration * 5

    # Add decoration to start and end of statement
    statement = "{}  {}  {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""

# Displays instructions / information
def instructions():

    statement_generator("Instructions / Information", "=")
    print()
    print("Please enter a factor")
    print()
    print("This program will show all off the factors for that number.")
    print()
    print("Complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to quit. ")
    print()
    return ""

# Checks input is a number more than a given value
def num_check(question, low):

    valid = False
    while not valid:

        error = "please insert a number that is more than (or equal to) {}".format(low)

        try:

            # ask user to enter a number
            response = int(input(question))

            # checks number is more than zero 
            if response >= low:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)

# Get factors, returns a sorted list


    num_lollies = int(input("How many lollies? "))
    num_students = int(input("How many students? "))

    # Lollies per student (divide)
    lollies_per_student = num_lollies // num_students
    lollies_left = num_lollies % num_students

    # Output fixer (lolly vs lollies)
    if lollies_left == 1:
        lolly_pl = "lolly"
    else:
        lolly_pl = "lollies"

    # Output
    print()
    print("You have {} lollies and {} student."
          .format(num_lollies, num_students))
    print("Each student gets {} lollies".format(lollies_per_student))
    print("You have {} {} left".format(lollies_left, lolly_pl))
    print()

    keep_going = input("Again <enter>? ")
    print()

# Get factors
def get_factors(to_factor):
    if to_factor == 1:
        return [1]

    # Use (math. ) for  calculations for ciel of (x) and for square root

    my_list = []
    num_sqrt = math.ceil(math.sqrt(to_factor))

    # +1 for expanding range
    for num in range(1, num_sqrt + 1):
        if to_factor % num == 0:

            # find factor by division, get whole number only
            a_factor = to_factor // num

            my_list.append(a_factor)

            if num not in my_list:
                my_list.append(num)

    my_list.sort()

    # Unique factor stored here
    # my_list = list(set(my_list))
    return my_list

# Main routine goes here

# Heading
statement_generator("Factors Calculator", "-")

# Display instructions if user has not used the program before
first_time = input("Press <enter> to see the instructions or any key to continue. ")

if first_time == "":
    instructions()

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    comment = ""

    # Ask user for number to be factored...
    var_to_factor = num_check("Number? ", 2)

    if var_to_factor != 1:
        factor_list = get_factors(var_to_factor)
    else:
        factor_list = ""
        comment = "One is UNITY! It only has one factor. Itself :)"

    # comments for squares / primes
    if len(factor_list) == 2:
        comment = "{} is a prime number.".format(var_to_factor)
    elif len(factor_list) % 2 ==1:
        comment = "{} is a perfect square.".format(var_to_factor)

    # Output factors and comment
    # Generate heading...
    if var_to_factor == 1:
        heading = "One is special..."

    else:
        heading = "Factors of {}".format(var_to_factor)

    # Output factors and comment
    statement_generator(heading, "*")
    print()
    print(factor_list)
    print(comment)
    print()
    keep_going = input("Press <enter> to continue or any key to quit ")
    print()

print()
print("Thank you for using the factors calculator")
print()