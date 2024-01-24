def soal21(track):
    st = 0
    path = []

    for i, elem in enumerate(track):
        if elem == 'O':
            if st < 2:
                return "FAILED"
            st -= 2
            path.append("J")
        else:
            st += 1
            path.append("W")

    return path

div = "--------------------------------------------------------------------------------"
print(div)
track1 = [" ", " ", " ", " ", " ", "O", " ", " ", " ", "Finish"]
result1 = soal21(track1)
print("Contoh 1:", result1)
print(div)
track2 = [" ", "O", " ", " ", " ", " ", "O", " ", " ", "Finish"]
result2 = soal21(track2)
print("Contoh 2:", result2)
print(div)