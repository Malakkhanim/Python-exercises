factorial=1
while True:
    say=int(input("Ededi daxil edin:"))
    if (say <= 0):
        print("Sifirdan boyuk eded daxil edin!!!")
    else:
        for i in range(1,say+1):
            factorial=factorial*i
        print("Faktorial",factorial)
        break
