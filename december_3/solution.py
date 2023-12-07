
import os

relative_path = "input.txt"

absolute_path = os.path.abspath(os.path.join(os.path.dirname(__file__), relative_path))

with open(absolute_path) as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

# s = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598.."""

# lines = s.split("\n")

# lines = lines[:6]
m = len(lines)
n = len(lines[0])
sum_ = 0 

hm = {} 

uniq = 0 
for i in range(m): 
    
    number = 0 
    visited = set() 
    for j in range(n): 
        if lines[i][j].isnumeric(): 
            number = number*10 + int(lines[i][j])
            visited.add((i,j))
            if j == n-1 : 
                final_n = number 
                uniq+=1  
                for (x,y) in visited : 
                    hm[(x,y)] = (final_n,uniq)
                   
                
                
        else : 
            final_n = number 
            # print(final_n,visited )
            if final_n == 0 : continue 
            uniq+=1  
            for (x,y) in visited : 
                    hm[(x,y)] = (final_n,uniq)

            number = 0 
            visited = set() 


for i in range(m): 
    for j in range(n): 
        a = set()
        a_s = set()
        if lines[i][j] == "*": 
            for dx,dy in [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]: 
                if (i+dx,j+dy) in hm: 
                    val,u = hm[(i+dx,j+dy)]
                    a.add(val)
                    a_s.add(u)
  
        a = list(a)
        if len(a_s) == 2 : 
            sum_ += (a[0]*a[1])



print(sum_)
                        

