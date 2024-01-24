def soal13(waktu):
    arr_jam = waktu.split(":")
    #* Separate By Hours and Minutes
    #* 1hour = 360/12 = 30. this is conts
    #* 1minute = 360/60 = 6, this also conts
    j_pendek = int(arr_jam[0])
    j_panjang = int(arr_jam[1])

    s_jpen = j_pendek*30 + (j_panjang/60)*30
    s_jpan = j_panjang*6

    Sudut = int(s_jpan - s_jpen)
    div = "-------------------------------------------------------------"
    print(div)
    if (Sudut < 0):
        print("Input Jam : " + waktu)
        print("Output Sudut : " + str(Sudut * -1))
    else:
        print("Input Jam : " + waktu)
        print("Output Sudut : " + str(Sudut))
    print(div)

soal13("3:00")
soal13("5:30")
soal13("2:20")