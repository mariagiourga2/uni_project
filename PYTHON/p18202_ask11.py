def sos():
    lst = []
    length = int(input("Enter list length: "))
    for i in range(0,length):
        letter = str(input())
        lst.append(letter)

    print("List:",lst)
    for i in range(0,length):
        x1=lst[i]
        x2=lst[i+1]
        x3=lst[i+2]
        print(x1,x2,x3)
        if (x1=="s"):
            if(x2=="o"):
                if(x3=="s"):
                    print("sos found")
sos()
