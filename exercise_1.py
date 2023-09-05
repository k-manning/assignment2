def get_unique_list(k):
    new_list = []
    for nums in k:
        if nums not in new_list:
            new_list.append(nums)
    return new_list
my_list = [1, 2, 3, 2, 1, 4]
unique_list= get_unique_list(my_list)
print(unique_list)
