
kata = str(input("Input Kata: "))

arr_kata = list(kata.lower())
n = len(arr_kata) - 1
i = 0

polindrom = True
while i <= n:
    if arr_kata[i] != arr_kata [n]:
        polindrom = False
        break
    n-=1
    i+=1

if polindrom == True:
    print("'" + kata + "'" + " adalah Polindrom")
else:
    print("'" + kata + "'" + " Bukan Polindrom")
