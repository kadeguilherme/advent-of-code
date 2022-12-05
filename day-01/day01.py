arq = open("day01.txt", "r")
linha = arq.read().splitlines()
calories = []
loslElement = 0
for i in linha:
    if i == "":
        calories.append(loslElement)
        loslElement = 0
        continue
    loslElement += int(i)

# PARTE 1 DO DESAFIO
calories.append(loslElement)
print(f'Elf carrying the most Calories:', max(calories))

# PARTE 2 DO DESAFIO
topthree = []
calories = sorted(calories)
for i in range(0, 3):
    topthree.append(calories.pop())
print(f'Total top three Elves carrying the most Calories: ', sum(topthree))
