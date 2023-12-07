
import os

relative_path = "input.txt"

absolute_path = os.path.abspath(os.path.join(os.path.dirname(__file__), relative_path))

with open(absolute_path) as file:
    lines = file.readlines()

# example = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

# lines = example.split("\n")

# threshold = {"red":12, "blue":14 ,"green":13}

example_String = "8 green, 6 blue, 2 red"

def isSetPossible(set_string): 
    hm = {}
    colors = set_string.split(",")

    for color in colors: 
        number,color_name = color.strip().split(" ")
        number = int(number)
        hm[color_name] = number
    return hm 

sum_ = 0 
for line in lines: 
    main_hm = {"red":float("-inf"), "blue":float("-inf") ,"green":float("-inf")}

    game_info = line.split(":")
    game_number = game_info[0].strip().split(" ")[1]
    game_number = int(game_number)
    subsets = game_info[1].strip().split(";")

    for subset in subsets:
        # print(subset)
        hm = isSetPossible(subset)

        for key,val in hm.items(): 
            main_hm[key] = max(val,main_hm[key])
    
    prod = 1 
    for val in main_hm.values(): 
        prod *= val 
    sum_ += prod 
            

print(sum_)


