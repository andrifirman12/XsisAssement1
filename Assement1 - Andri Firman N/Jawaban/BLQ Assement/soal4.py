n = int(input("Input Size N: "))

i = 1
bil = 1

#* Do Loop Until get N bilangan Prima
while i <= n:
    hb=0
    for k in range(1, bil):
        if bil >= 2:
            if bil%k == 0:
                hb+=1
    if hb == 1:
        print(bil)
        i+=1
    bil = bil+1