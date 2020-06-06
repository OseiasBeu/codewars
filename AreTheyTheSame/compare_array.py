def comp(arr1, arr2):
    if arr1 is None or arr2 is None:
        return False
    array1 = []
    array2 = []
    
    for i in arr1:
        p = str(i).replace('-','')
        array1.append(int(p))
        array1.sort()
    for i in arr2:
        p = str(i).replace('-','')
        array2.append(int(p))
        array2.sort()
    print('O array1 ordenado é:{}'.format(array1))
    print('O array2 ordenado é:{}'.format(array2))
    aux = []
    if array1 is None or array2 is None:
        return False
    if len(array1) != len(array2):
        return False
    if array1 == array2:
        return True
    
    for n in array1:
       aux.append(int(n**2))

    aux.sort()
    array2.sort()
    print(aux)
    print(array2)

    if array2 == aux:
        response = True
    else:
        response = False

    return response


a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
print(comp(a1, a2))  # Return this function is: True

b1 = [11, 19, 19, 19, 121, 144, 144, 161]
b2 = [-161, -144, -144, -121, -11, 19, 19, 19]
# print(comp(b1, b2))  # Return this function is: True

c1 = [80, 85, 12, 59]
c2 = [6400, 7225, 144, 3482]
# print(comp(c1, c2))  # Return this function is: False

d1 = [53, 96, 46, 39, 84, 58, 9]
d2 = [2809, 9216, 2116, 1522, 7056, 3364, 81]
# print(comp(d1, d2))  # Return this function is: False

e1 = [86, 66, 16, 69, 91]
e2 = [7396, 4356, 257, 4761, 8281]
# print(comp(e1, e2))


#Other functions:
# def comp(array1, array2):
#     try:
#         return sorted([i ** 2 for i in array1]) == sorted(array2)
#     except:
#         return False

# def comp(a1, a2):
#     return None not in (a1,a2) and [i*i for i in sorted(a1)]==sorted(a2)
# from collections import Counter as c
# def comp(a1, a2):
#     return a1 != None and a2 != None and c(a2) == c( elt**2 for elt in a1 )