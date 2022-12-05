arq = open("day01.txt", "r")
linha = arq.read().splitlines()
soma = []
aux = 0
for i in linha:
    if i == "":
        soma.append(aux)
        aux = 0
        continue
    aux += int(i)

valor = max(soma) if (max(soma) > aux) else aux

print(valor)
