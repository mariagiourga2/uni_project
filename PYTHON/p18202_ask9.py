def pair():
    lst = []
    length = int(input("Enter list length: "))
    for i in range(0,length):
        num = int(input())
        lst.append(num)

    print("List:",lst)
    t = int(input("Enter t: "))
    print(t)
    lst2 = []
    final = []
    sum = 0
    length2 = 0
    for i in range(0,length):
        x = lst[i]
        #print(x)
        for j in range(0,length):
            if i!=j:
                sum = x + lst[j]
                print(x,"+",lst[j],"=",sum)
                if (sum == t):
                    if lst[i] not in lst2:
                        lst2.append(lst[i])
                        length2 = length2 + 1
                    if lst[j] not in lst2:     
                        lst2.append(lst[j])
                        length2 = length2 + 1
    print("remove: ",lst2)


    for item1 in lst:
        for item2 in lst2:
            if item1==item2:
                lst.remove(item2)

    print("final list: ",lst)

pair()
