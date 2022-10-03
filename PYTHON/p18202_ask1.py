def gargame():
    a = int(input())
    b =  int(input())

    for i in range(a,b):
        number = i
        i = [int(x) for x in str(i)]
        listLenth = len(i)
        if listLenth == 1:
            s = i[0]**1
        elif listLenth == 2:
            s = i[0]**1 + i[1]**2
        elif listLenth == 3:   
            s = i[0]**1 + i[1]**2 + i[2]**3
        elif listLenth == 4:
            s = i[0]**1 + i[1]**2 + i[2]**3 + i[3]**4
        elif listLenth == 5:
            s = i[0]**1 + i[1]**2 + i[2]**3 + i[3]**4 + i[4]**5
        elif listLenth == 6:
            s = i[0]**1 + i[1]**2 + i[2]**3 + i[3]**4 + i[4]**5 + i[5]**6
        elif listLenth == 7:
            s = i[0]**1 + i[1]**2 + i[2]**3 + i[3]**4 + i[4]**5 + i[5]**6 + i[6]**7

        if s == number:
            print(number)
gargame()
