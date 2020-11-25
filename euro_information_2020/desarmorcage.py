import itertools

n = int(input())
init_regs = list(map(int, input().strip().split()))
instructions = [input().strip().split() for _ in range(n)]
final_regs = list(map(int, input().strip().split()))
i_reg = lambda c: ord(c) - ord('A')
for l in range(n):
    for comb in itertools.combinations(range(n), r=l):
        regs = init_regs[:]
        for i in comb:
            ins = instructions[i]
            if ins[0] == 'ADD':
                regs[i_reg(ins[3])] = regs[i_reg(ins[1])] + regs[i_reg(ins[2])]
            elif ins[0] == 'MOV':
                regs[i_reg(ins[2])] = regs[i_reg(ins[1])]
                regs[i_reg(ins[1])] = 0
            else:
                regs[i_reg(ins[2])] = regs[i_reg(ins[1])]
        if regs == final_regs:
            print(" ".join(map(lambda v: f"{v + 1}", set(range(n)) - set(comb))))
            exit()
