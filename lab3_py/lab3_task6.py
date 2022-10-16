list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_ = 0
ind_max_ = 0
for ind,val in enumerate(list_numbers):
    if val > max_:
        max_ = val;
        ind_max_ = ind

list_numbers[ind_max_],list_numbers[-1] = list_numbers[-1],max_
print(list_numbers)
