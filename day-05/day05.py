with open("day05.txt", 'r') as arq:

    index_strings, instrucs = [i.splitlines()
                               for i in arq.read().strip('\n').split('\n\n')]
    stacks = {int(digit): [] for digit in index_strings[-1].replace(" ", "")}
    # Estou pegando a posição que se encontra os numero: 1,2,3, .. 9 no array
    position_stacks = [index for index, char in enumerate(
        index_strings[-1]) if char != ' ']

    # Percorrendo o index_strings e position_stacks verifico se na string[index] está vazio, caso contrario possui uma string e add
    # no dicionario
    for string in index_strings[:-1]:
        num = 1
        for index in position_stacks:
            if string[index] != " ":
                stacks[num].insert(0, string[index])
            num += 1

    for instruc in instrucs:
        quant, stack1, stack2 = int(instruc.split(' ')[1]), int(instruc.split(
            ' ')[3]), int(instruc.split(' ')[-1])
        for i in range(quant):
            stacks[stack2].append(stacks[stack1].pop())

for stack in stacks:
    print(stacks[stack][-1], end="")
print("")
