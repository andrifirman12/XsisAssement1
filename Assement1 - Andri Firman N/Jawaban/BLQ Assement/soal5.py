n = int(input("Input Size N: "))
a = 0
b = 1

#* Do Loop Until get N Fibonanci
for i in range(n):
    print(a)
    c = a+b
    a = b
    b = c