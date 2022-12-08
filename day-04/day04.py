range_equal = 0
without_comma = list()
with open("day04.txt", "r") as arq:
    data = [i for i in arq.read().split('\n')]

    list_one = list()
    list_two = list()

    for c, v in enumerate(data):
        without_comma.append(v.split(','))

    for c, v in enumerate(without_comma):
        value_first = int(v[0].replace('-', ' ').split(' ')[0])
        value_last = int(v[0].replace('-', ' ').split(' ')[1])
        value_first2 = int(v[1].replace('-', ' ').split(' ')[0])
        value_last2 = int(v[1].replace('-', ' ').split(' ')[1])

        for i in range(value_first, value_last+1):
            list_one.append(i)

        for i in range(value_first2, value_last2+1):
            list_two.append(i)

        if set(list_one).issuperset(set(list_two)) or set(list_two).issuperset(set(list_one)):
            range_equal += 1
        list_one = []
        list_two = []
print(range_equal)
