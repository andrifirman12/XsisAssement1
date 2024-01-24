def soal10(name):
    arr_name = name.split(" ")
    print("Input : " + str(name))
    print("Output : ", end="")
    for i in range(0, len(arr_name)):
        top = len(arr_name[i])
        bottom = 0;
        for j in range(bottom, top):
            if j == bottom or j == top-1:
                print(arr_name[i][j], end="")
            else:
                print("*", end="")
        print(" ", end=" ")
    print("\n")

soal10("Susilo Bambang Yudhoyono")
soal10("Rani Tiara")
soal10("Andri Firman Nurvianto")