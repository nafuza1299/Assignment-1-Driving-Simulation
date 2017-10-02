def modulo42():
    list = []
    for i in range(1, 11):#range from 1 to 10 including 10
        i = int(input())
        n = i % 42
        list.append(n)
    print(len(set(list))) #len would only count set of unique and distinct result
modulo42()

