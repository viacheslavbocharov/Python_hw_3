# lst = []
# lst = [1, 2, 3, 4, 5, 6, 7, 8]
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_lst = None

if len(lst) == 0:
    new_lst = [[], []]
elif len(lst)%2 == 0:
    new_lst = [lst[:len(lst) // 2], lst[len(lst) // 2:]]
else:
    new_lst = [lst[:(len(lst)+1) // 2], lst[(len(lst)+1) // 2:]]

print("Origin list: ", lst)
print("Modified list: ", new_lst)