def sum_numbers(n):
    n_str = str(n)
    j = 0 
    r = 0
    for i in n_str:
        r = j+int(i)
        j = r
    return j

def digital_root(n):
    # ...
    res = n
    numberString = str(n)
    lengthInput =  len(numberString)
    while (int(lengthInput) > 1):
        response =  sum_numbers(numberString)
        numberString = response
        lengthInput = len(str(response))                    
        res = response
    return res


print(digital_root(16)) # return number: 7
print(digital_root(6)) # return number:  6
print(digital_root(942)) # return number: 6
print(digital_root(132189)) # return number: 6
print(digital_root(493193)) # return number: 2


# others resolutions
#     def digital_root(n):
#        return n if n < 10 else digital_root(sum(map(int,str(n))))

    # def digital_root(n):
        # return n if n < 10 else digital_root(sum([int(c) for c in str(n)]))