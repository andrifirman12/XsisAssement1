def soal11(word):
    len_word = len(word)
    i = len_word - 1
    side = int(len(word) / 2)

    print("Input : " + word)
    print("Output : ")
    while i >= 0:
        for j in range(side):
            print("*", end="")
        print(word[i], end="")
        for k in range(side):
            print("*", end="")
        print()
        i -= 1

    print()

soal11("Afrika")
soal11("Jeruk")