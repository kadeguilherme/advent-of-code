
with open("day06.txt", "r") as f:
    arq = f.readlines()
    position_current = 0
    list_characters = []
    position_characters = 0
    for i in arq[0]:
        list_characters = []
        position_current = position_characters

        for d in range(4):
            list_characters.append(arq[0][position_current])
            position_current += 1

        if len(set(list_characters)) == 4:
            print(position_current)
            break
        position_characters += 1
# BUG lista_characters.append(arq[0][position_current]) IndexError: string index out of range
