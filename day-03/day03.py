total = 0
sumtotal = 0
lower_letters = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
                 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
upper_letters = {'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36,
                 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}
with open("day03.txt", "r") as f:
    linha = f.readline().strip('\n')

    while linha:

        firstpar, secondpart = linha[:len(linha)//2], linha[len(linha)//2:]
        source_letter = ''
        for i in firstpar:
            for j in secondpart:
                if i == j:
                    source_letter = i
                    break
        if source_letter in lower_letters:
            total += lower_letters[source_letter]
        if source_letter in upper_letters:
            total += upper_letters[source_letter]
        linha = f.readline().strip('\n')

print(total)

# PARTE 2 DO DESAFIO
with open("day03.txt", "r") as f:
    data = [i for i in f.read().split('\n')]
    j = 3
    for i in range(0, len(data), 3):
        rockseat = data[i:j]
        source_letter = ''
        for first in rockseat[0]:
            for second in rockseat[1]:
                for third in rockseat[2]:
                    if first == second and first == third:
                        source_letter = first

        if source_letter in lower_letters:
            sumtotal += lower_letters[source_letter]
        if source_letter in upper_letters:
            sumtotal += upper_letters[source_letter]
        j += 3
print(sumtotal)
