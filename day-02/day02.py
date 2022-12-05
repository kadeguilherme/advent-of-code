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
