
import os

relative_path = "input.txt"

absolute_path = os.path.abspath(os.path.join(os.path.dirname(__file__), relative_path))

with open(absolute_path) as file:
    lines = file.readlines()


sum_ = 0 

digits = ["one","two","three","four","five","six","seven","eight","nine"]
digits_set = set(digits)
digits_hm = {val:i+1 for i,val in enumerate(digits)}

for line in lines: 
    num1 = None
    num2 = 0  
    for i in range(len(line)): 
        if line[i].isnumeric(): 
            if not num1: 
                num1 = int(line[i]) 
            num2 = int(line[i])
        else : 
            for j in range(1,6):
                if line[i:i+j] in digits_hm: 
                    if not num1: 
                        num1 = digits_hm[line[i:i+j]]
                    num2 = digits_hm[line[i:i+j]]

    sum_ += num1*10 + num2

print(sum_)