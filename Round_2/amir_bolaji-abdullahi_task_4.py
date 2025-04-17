def second_largest(lst): 
    res = sorted(lst, reverse=True)
    return res[1]
print(second_largest(lst))
