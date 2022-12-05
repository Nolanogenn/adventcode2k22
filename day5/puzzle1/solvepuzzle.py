data = open('input.txt').readlines()

crates = [d.replace('\n', '') for d in data[:8]]
moves = [d.replace('\n', '') for d in data[10:]]
stacks = {x:[] for x in range(1,10)}

for crate in crates:
    for i, char in enumerate(crate[1::4], start=1):
        if char != ' ':
            stacks[i].insert(0, char)

for move in moves:
    compressed_move = [int(x) for x in move.split() if x.isnumeric()]
    movement = compressed_move[0]
    source = compressed_move[1]
    print(move)
    target = compressed_move[2]
    for m in range(movement):
        tomove = stacks[source].pop()
        stacks[target].append(tomove)


for stack in stacks:
    print(stacks[stack][-1])