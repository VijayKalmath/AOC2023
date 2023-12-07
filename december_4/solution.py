
import os

relative_path = "input.txt"

absolute_path = os.path.abspath(os.path.join(os.path.dirname(__file__), relative_path))

with open(absolute_path) as file:
    lines = file.readlines()


# s = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

# lines = s.split("\n")

s_ = 0 
hm = {} 

for i,line in enumerate(lines): 
    queue = [i]

    while queue: 
        s_ += 1 
        index = queue.pop()

        if index in hm : 
            count = hm[index]
        else : 
            w_n, n = lines[index].split(" |")[0], lines[index].split(" |")[1]
            w_n = set([int(x) for x in w_n.split(": ")[1].split()])

            n = [int(x) for x in n.split()]
            count = 0 
            for x in n: 
                if x in w_n: 
                    count +=1 
            hm[index] = count 
        
        for i in range(1,count+1):
            queue.append(index+i) 
    
print(s_)


