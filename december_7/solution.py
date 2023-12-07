
import os

relative_path = "input.txt"

absolute_path = os.path.abspath(os.path.join(os.path.dirname(__file__), relative_path))

with open(absolute_path) as file:
    lines = file.readlines()

s = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

# lines = s.split("\n")

# classify each into type 
hm = {"5":7,
      "4":6,
      "F":5,
      "Three":4,
      "Two": 3, 
      "One": 2 , 
      "High" : 1} 

from collections import Counter
def get_type(card): 
    # card= T55J5 
    card_list = list(card) 
    counter = Counter(card_list)
    if len(counter) == 1 : 
        return 7 
    j_count = counter.get("J",0)
    if j_count:  counter.pop("J")

    pair_count = 0 
    three_count = 0 
    four_count = 0 
    for _,v in counter.items(): 
        if v == 4 : 
            four_count = 1 
        if v == 3: 
            three_count +=1
        elif v == 2 : 
            pair_count += 1 

    if j_count == 0 : 
        if four_count : return 6 
        if three_count == 1 and pair_count == 1 : return 5 
        if three_count == 1 : return 4 # three count 
        if pair_count == 2 : return 3 
        if pair_count == 1 : return 2
        return 1 

    else : 
        if j_count == 5 or j_count == 4 : 
            return 7 
        if j_count == 3 : 
            if pair_count == 1 : return 7 
            if pair_count == 0 : return 6

        if j_count == 2 : 
            if three_count == 1 : return 7 
            if pair_count == 1 : return 6 
            if pair_count == 0 : return 4 # three of a kind 
        
        if j_count == 1 : 
            if four_count == 1  : return 7 
            if three_count == 1 : return 6 
            if pair_count == 2 : return 5 
            if pair_count == 1 : return 4 
            if pair_count == 0 : return 2 
    
order = "A,K, Q, T, 9, 8, 7, 6, 5, 4, 3,2,J" 

order = [x.strip() for x in order.split(",")]
order_hm = {x: len(order) - i for i,x in enumerate(order)}

print(order_hm)

card_tuple = [] 
for line in lines: 
    card,bid = line.split() 
    card_tuple.append((get_type(card),card,int(bid) ))

# card_tuple =[(4, 'A55J5', 684), (4, '2QQJA', 483)]

card_tuple = sorted(card_tuple,key = lambda x : (x[0],[order_hm[c] for c in x[1]]),reverse=True)

print(card_tuple)

for card in card_tuple: 
    print(card)
len_= len(lines)

complete_= 0 

for i,val in enumerate(card_tuple): 
    rank = len_ - i 
    complete_ += val[2]*rank

print(complete_)