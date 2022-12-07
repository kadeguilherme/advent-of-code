# A, X -> Rock
# B, Y -> Paper
# C, Z -> Scissors

arq = open("day02.txt", "r")
linhas = arq.readline()
totalscore = 0

while linhas:
    linha = linhas.split()
    if linha[0] == 'A' and linha[1] == 'X':
        totalscore += 1 + 3
    elif linha[0] == 'A' and linha[1] == 'Y':
        totalscore += 2 + 6
    elif linha[0] == 'A' and linha[1] == 'Z':
        totalscore += 3

    if linha[0] == 'B' and linha[1] == 'X':
        totalscore += 1
    elif linha[0] == 'B' and linha[1] == 'Y':
        totalscore += 2 + 3
    elif linha[0] == 'B' and linha[1] == 'Z':
        totalscore += 3 + 6

    if linha[0] == 'C' and linha[1] == 'X':
        totalscore += 1 + 6
    elif linha[0] == 'C' and linha[1] == 'Y':
        totalscore += 2
    elif linha[0] == 'C' and linha[1] == 'Z':
        totalscore += 3 + 3
    linhas = arq.readline()
print(totalscore)

# PARTE 2

arq = open("day02.txt", "r")
linhas = arq.readline()
totalscoredesired = 0

while linhas:
    linha = linhas.split()
    if linha[0] == 'A' and linha[1] == 'X':
        totalscoredesired += 3
    elif linha[0] == 'A' and linha[1] == 'Y':
        totalscoredesired += 1 + 3
    elif linha[0] == 'A' and linha[1] == 'Z':
        totalscoredesired += 2 + 6

    if linha[0] == 'B' and linha[1] == 'X':
        totalscoredesired += 1
    elif linha[0] == 'B' and linha[1] == 'Y':
        totalscoredesired += 2 + 3
    elif linha[0] == 'B' and linha[1] == 'Z':
        totalscoredesired += 3 + 6

    if linha[0] == 'C' and linha[1] == 'X':
        totalscoredesired += 2
    elif linha[0] == 'C' and linha[1] == 'Y':
        totalscoredesired += 3 + 3
    elif linha[0] == 'C' and linha[1] == 'Z':
        totalscoredesired += 1 + 6
    linhas = arq.readline()

print(totalscoredesired)
