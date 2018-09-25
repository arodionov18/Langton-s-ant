import collections as coll
import sys

def right_turn(vector):
    if vector == north:
        return east
    elif vector == east:
        return south
    elif vector == south:
        return west
    else:
        return north

def left_turn(vector):
    if vector == north:
        return west
    elif vector == west:
        return south
    elif vector == south:
        return east
    else:
        return north
    
def turn(vector, rule):
    if rule == 'L':
        return left_turn(vector)
    else:
        return right_turn(vector)

def step_forward(position, vector):
    if vector == north:
        position[1] += 1
    elif vector == east:
        position[0] += 1
    elif vector == south:
        position[1] -= 1
    else:
        position[0] -= 1
    return position            

def cycle_step(step_number):
    global current_position, current_vector, field, is_infinite
    for i in range(length):
        current_vector = turn(current_vector, chain[i])
        new_shifts = []
        if step_number == length + 1:
            last_step_cells.add(tuple(current_position))
        if tuple(current_position) not in field.keys():
            field[tuple(current_position)] = [t for t in range(len(rule))]
        for j in range(len(field[tuple(current_position)])):
            current_shift = field[tuple(current_position)][j]
            if rule_shifts[current_shift][0] == chain[i]:
                new_shifts.append((current_shift + 1) % len(rule))
        if len(new_shifts) == 0:
            is_infinite = False
            return
        field[tuple(current_position)] = new_shifts
        current_position = step_forward(current_position, current_vector)
    

def main():
    global rule, field, rule_shifts, current_position, current_vector, is_infinite, length, chain, last_step_cells
    
    field = dict()
    current_position = [0, 0]
    current_vector = north
    
    if abs(chain.count('L') - chain.count('R')) % 4 != 0:
        print(chain, "It's not infinite")
    else:
        is_infinite = True
        length = len(chain)
        step_number = 1
        while is_infinite and step_number <= length + 1:
            cycle_step(step_number)
            step_number += 1
        if is_infinite:
            count_of_paints = 1
            for cell in last_step_cells:
                count_of_paints *= len(field[cell])
            print(chain, "It's infinite and there are " + str(count_of_paints) + " variants of field color")
            #print(chain, "It's infinite")
        else:
            print(chain, "It's not infinite")

rule = "LLLRRR "
file_in = open("sequences.txt", 'r')
sys.stdout = open(rule + "_result.txt", 'w')
north = "north"
east = "east"
west = "west"
south = "south"


print(rule)

vectors = dict()
vectors[north] = 0
vectors[east] = 1
vectors[south] = 2
vectors[east] = 3

rule_shifts = [""] * len(rule)
rule_shifts[0] = rule
for i in range(1, len(rule)):
    rule_shifts[i] = rule_shifts[i - 1][1:] + rule_shifts[i - 1][0]

field = dict()
current_position = [0, 0]
current_vector = north


for line in file_in:
    chain = line.strip()
    is_infinite = True
    last_step_cells = set()
    length = len(chain)
    main()

        
        
#"LRRRRLLRRLRLLRLLRLRLLRRRRLLRLLRRRRLLRRRRLLRLRRRRLRLLLLRRRRLRRLRRRRLLLLRLRRRRLRRRRLLLLRLRRRRLRLLRRLLLLRRL"