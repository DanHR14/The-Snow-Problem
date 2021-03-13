walls = (0, 1, 0, 2, 1, 0, 3, 2, 1, 1, 1, 5, 0, 1)

def snow_stored_cuadratic(walls):
    snow_stored = 0
    max_height = max(walls)
    
    print(max_height)
            
    while (max_height > 0):
        find_wall = False
        brick = 0
        for wall in walls:
            if wall >= max_height:
                find_wall = True
                snow_stored += brick 
                brick = 0
                continue
            if find_wall:
                brick += 1
        max_height -= 1
                
    return snow_stored

print(snow_stored_cuadratic(walls))
