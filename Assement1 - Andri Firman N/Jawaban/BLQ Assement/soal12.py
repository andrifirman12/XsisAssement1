deret = '1 2 1 3 4 7 1 1 5 6 1 8'
arr_list = list(map(int, deret.split(" ")))

def quicksort(arr_list, asc):

    if len(arr_list) <= 1:
        return arr_list
    else:
        pivot = arr_list.pop()

    greater = []
    lower = []

    for x in arr_list:
        if x > pivot:
            greater.append(x)
        else:
            lower.append(x)

    if asc == True:
        final = quicksort(lower, asc) + [pivot] + quicksort(greater, asc)
    else:
        final = quicksort(greater, asc) + [pivot] + quicksort(lower, asc)
    return final

div = "-------------------------------------------------------------"
print(div)
print("Input Array: ", end=" ")
print(arr_list)
print(div)
print("Desc Sort : ", end=" ")
print(quicksort(arr_list, asc=False))
print("Asc Sort : ", end=" ")
print(quicksort(arr_list, asc=True))
print(div)