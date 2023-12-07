import os 
relative_path = "input.txt"

absolute_path = os.path.abspath(os.path.join(os.path.dirname(__file__), relative_path))


with open(absolute_path) as file:
    lines = file.read() 
    lines = lines.split("\n\n")

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

# lines = s.split("\n\n")

seeds = lines[0]
seeds = [int(x) for x in lines[0].split(": ")[1].strip().split(" ")]
s_new = [] 

for i in range(0,len(seeds),2): 
    s_new.append((seeds[i], seeds[i] + seeds[i+1]))

seeds = s_new 

blocks = lines[1:]
# print(seeds,blocks)
# print(blocks)

for block in blocks:
    ranges = []  
    for line in block.splitlines()[1:]: 
        ranges.append(list(map(int,line.split())))
    
    new = [] 

    while seeds: 
        s,e = seeds.pop() 
        for a,b,c in ranges: 
            o_s = max(s, b)
            o_e = min(e, b+c)
            if o_s < o_e : 
                new.append((o_s-b+a, o_e - b +a ))
                if o_s > s : 
                    seeds.append((s,o_s))
                if e > o_e: 
                    seeds.append((o_e,e))
                break
        else: 
            new.append((s,e))
    
    seeds = new

print(seeds)
print(min(seeds))

