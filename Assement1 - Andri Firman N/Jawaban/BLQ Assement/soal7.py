deret = '8 7 0 2 7 1 7 6 3 0 7 1 3 4 6 1 6 4 3'
arr = list(map(int, deret.split(" ")))
arr_len = len(arr)
s_arr = sorted(arr, key=int, reverse=False)

#* Mean
mean = int(sum(arr) / arr_len)

#* Median
if arr_len % 2 == 0:
    median1 = s_arr[arr_len//2]
    median2 = s_arr[arr_len//2 - 1]
    if median1 > median2:
        median = median2
else:
    median = s_arr[arr_len//2]

#* Modus
holder = {}
for i in range(0, arr_len):
    if s_arr[i] in holder:
        holder[s_arr[i]] +=1
    else:
        holder[s_arr[i]] =1

modus = max(holder, key=holder.get)

#* Print Result
div = "-------------------------------------------------------------"
print(div + "\nArray: ")
print(arr)
print("Sorted Array: ")
print(s_arr)
print(div + "\nMean : " + str(mean))
print("Median : " + str(median))
print("Modus : " + str(modus) + "\n" + div)
