i, dan=0,0


def gugudan(dan):
    for i in range(1,10):
        print("%d X %d=%2d"%(dan,i,dan*i))


while True:
    dan=int(input("몇 단?"))
    if(dan >= 2 and dan<=9):
     gugudan(dan)
    else:
        break

    