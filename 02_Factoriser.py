to_factor = 12

factors_list = []

for item in range(1, to_factor + 1):
    if to_factor % item == 0:
        factors_list.append(item)



print(factors_list)