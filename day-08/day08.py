with open("day08.txt", "r") as file:
    matriz = []
    edge = 0
    total = 0

    for line in file:
        lista = list(map(int, line.rstrip()))
        matriz.append(lista)

    # COUNT EDGES
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j == 0:
                edge += 1
            if j == len(matriz[i]) - 1:
                edge += 1
    total_edge = edge + len(matriz[-1])-2 + len(matriz[0])-2

    ROWS = len(matriz)
    COLUMNS = len(matriz)

    for row in range(1, ROWS - 1):
        for column in range(1, COLUMNS - 1):
            right = [matriz[row][i] for i in range(column+1, COLUMNS)]
            left = [matriz[row][i] for i in range(0, column)]
            down = [matriz[i][column] for i in range(row+1, ROWS)]
            up = [matriz[i][column] for i in range(0, row)]
            current = matriz[row][column]

            if max(right) < current or max(left) < current or max(down) < current or max(up) < current:
                total += 1
    print(total + total_edge)


# PART2
