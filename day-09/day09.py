with open("day09.txt", "r") as file:
    data = []
    for line in file:
        data.append(line.rstrip().split(" "))
    H = [0, 0]
    T = [0, 0]
    pontos_T = []
    for directions, value in data:
        if directions in ['R', 'L']:
            move, direc = ('x', 1) if directions == 'R' else ('x', -1)
        if directions in ['U', 'D']:
            move, direc = ('y', 1) if directions == 'U' else ('y', -1)
        for i in range(int(value)):
            if move == 'x':
                H[0] += direc
            if move == 'y':
                H[1] += direc
            for j in range(1, int(2)):
                if abs(T[0] - H[0]) > 1 and abs(T[1] - H[1]) == 0:
                    T[0] += direc
                elif abs(T[0] - H[0]) > 1 and abs(T[1] - H[1]) == 1:
                    T[0] += direc
                    T[1] = H[1]
                elif abs(T[1] - H[1]) > 1 and abs(T[0] - H[0]) == 0:
                    T[1] += direc
                elif abs(T[1] - H[1]) > 1 and abs(T[0] - H[0]) == 1:
                    T[1] += direc
                    T[0] = H[0]
                if T not in pontos_T:
                    x = T[0]
                    y = T[1]
                    pontos_T.append([x, y])

    print(len(pontos_T))
