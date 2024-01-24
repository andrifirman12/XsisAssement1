deret = '3 9 0 7 1 2 4'
arr_list = list(map(int, deret.split(" ")))

def soal14(n):
    left = []
    middle = []
    right = []

    for y in range(0, len(arr_list)):

        if y < n:
            right.append(arr_list[y])
        if y==n:
            left.append(arr_list[y])
        if y>n:
            middle.append(arr_list[y])

        new_list = left + middle + right
    return new_list

div = "-------------------------------------------------------------"
print(div)
print("Array Normal : ", end=" ")
print(arr_list)
print("Array Input 3 : ", end=" ")
print(soal14(3))
print("Array Input 1 : ", end=" ")
print(soal14(1))
print(div)