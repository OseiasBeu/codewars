def find_outlier(integers):
    # Odds or Evens
    odds = []
    evens = []
    for n in integers:
        if n%2 == 0:
            evens.append(n)
        else: 
            odds.append(n)    
    len_odds = len(odds)        
    len_evens = len(evens)
    
    if len_evens > len_odds:
        return odds[0]
    else: 
        return evens[0]
    
    return None


print(find_outlier([2, 4, 6, 8, 10, 3])) # Return number 3)
print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36])) #Return number 11
print(find_outlier([160, 3, 1719, 19, 11, 13, -21])) # Return number 160



# Others solutions:
# def find_outlier(int):
#     odds = [x for x in int if x%2!=0]
#     evens= [x for x in int if x%2==0]
#     return odds[0] if len(odds)<len(evens) else evens[0]