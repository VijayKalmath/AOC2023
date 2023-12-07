
import os

from numpy import number
from sympy import continued_fraction

relative_path = "input.txt"

absolute_path = os.path.abspath(os.path.join(os.path.dirname(__file__), relative_path))


with open(absolute_path) as file:
    lines = file.readlines()




s = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

# lines = s.split("\n")
print(lines[0])
seeds = [int(x) for x in lines[0].split(": ")[1].strip().split(" ")]


keys = ["seed","soil","fertilizer","water","light","temperature","humidity","location"]

hm = {key: {} for key in keys }

for line in lines[1:]: 
    if line == "\n": continue
    if not line : continue

    if line.startswith("seed-to-soil"): 
        key = "soil"
    elif line.startswith("soil-to-fertilizer"):
        key = "fertilizer"
    elif line.startswith("fertilizer-to-water"):
        key = "water"
    elif line.startswith("water-to-light "):
        key = "light"
    elif line.startswith("light-to-temperature"): 
        key = "temperature"
    elif line.startswith("temperature-to-humidity"):
        key = "humidity"
    elif  line.startswith("humidity-to-location"):
        key = "location"
    
    else : 
        # print(line.strip())
        numbers = [int(x) for x in line.strip().split(" ")]
        # print(numbers)

        hm[key][(numbers[1],numbers[1]+numbers[2]-1)] = numbers[0]
        

keys = ["seed","soil","fertilizer","water","light","temperature","humidity","location"]

# print(hm)
min_seed = float("inf")

i = 0 
for seed,seed_range in zip(seeds,seeds[1:]):
    if not i : 
        new_seeds = [seed, seed+seed_range-1]
        i = 1 
    else : 
        i = 0 
        continue
    
    dp = {} 
    print(new_seeds)
    for seed in new_seeds:
        # print("starting",seed)
        for key in keys: 
            # print("in", key,hm[key])
            for tuple,val in hm[key].items(): 
                if tuple[0] <= seed <= tuple[1] : 
                    seed = val + (seed - tuple[0]) 
                    
                    break
            # print("seed", seed)
        # break
        print("SEED",seed)
        min_seed = min(min_seed,seed)

print(min_seed)
    

    

