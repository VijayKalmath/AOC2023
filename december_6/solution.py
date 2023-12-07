
import os

relative_path = "input.txt"

absolute_path = os.path.abspath(os.path.join(os.path.dirname(__file__), relative_path))

with open(absolute_path) as file:
    lines = file.readlines()

s = """Time:      7  15   30
Distance:  9  40  200"""

# lines=s.split("\n")A

times,record_distance= lines[0],lines[1]

times = int(''.join(times.split(": ")[1].split()))
record_distance = int(''.join(record_distance.split(": ")[1].split()))

count = 0 
for x in range(times): 
    if x*(times-x) > record_distance:
        count +=1 


print(count)
    
