for i in range(0,5):
    for j in range(0,i):
        if i%2==0:
            print(j+1,"\t",end="")
        else:
            print("*","\t",end="")
    print("\n")