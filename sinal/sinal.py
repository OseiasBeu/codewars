def snail(snail_map):
    arr = []
    
    n = len(snail_map)
    
    y = 0
    x = -1
    
    DIR = 0 # 0 - EAST, 1 - SOUTH, 2 - WEST, 3 - NORTH
    
    seen = []
    
    if n == 1:
        return snail_map[0]
    
    def get_next_element():
        nonlocal x, y, DIR
        
        if DIR == 0:
            x += 1
            if (x, y) in seen:
                DIR = 1
                x -= 1
                return get_next_element()
            if x >= n:
                x = n - 1
                DIR = 1
        
        if DIR == 1:
            y += 1
            if (x, y) in seen:
                DIR = 2
                y -= 1
                return get_next_element()
            if y >= n:
                y = n -1
                DIR = 2
        
        if DIR == 2:
            x -= 1
            if (x, y) in seen:
                DIR = 3
                x += 1
                return get_next_element()
            if x < 0:
                x = 0
                DIR = 3
        
        if DIR == 3:
            y -= 1
            if (x, y) in seen:
                DIR = 0
                y += 1
                return get_next_element()
            if y < 0:
                y = 0
                DIR = 0
        
        seen.append((x, y))
        
        return snail_map[y][x]
        
                
    
    while len(arr) != n * n:
        arr.append(get_next_element())
    
    return arr