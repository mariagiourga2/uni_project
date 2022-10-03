def ROT13():
    word = str(input("Write a word:"))
    lst = []
    number = 0
    for i in word:
        lst.append(i)
    
    print("original list:",lst)
    ABC = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    newlst = []
    j=0
    k=0
    for letter in lst:
        if letter in ABC:
            j = ABC.index(letter)
            k=j+13
            #print(ABC[k])
            new= ABC[k]
            #print("word",new)
            newlst.append(new)

        if letter in abc:
            j = abc.index(letter)
            k=j+13
            #print(abc[k])
            new= abc[k]  
            newlst.append(new)

    print("New list",newlst)
ROT13()
