lst = [1, 2, 3, 4]
if len(lst) != 0:
    lst.insert(0, lst[-1])
    lst.pop()
print(lst)
