def hitung_gunung_dan_lembah(perjalanan):
    gunung = 0
    lembah = 0
    level = 0

    for langkah in perjalanan:
        if langkah == 'N':
            level += 1
        elif langkah == 'T':
            level -= 1

        # Cek apakah level kembali ke 0, dan tentukan apakah itu gunung atau lembah
        if level == 0:
            if langkah == 'N':
                lembah += 1
            elif langkah == 'T':
                gunung += 1

    return gunung, lembah


perjalanan_hattori = ['N', 'N', 'T', 'N', 'N', 'N', 'T', 'T', 'T', 'T', 'T', 'N', 'T', 'T', 'T', 'N', 'T', 'N']
jumlah_gunung, jumlah_lembah = hitung_gunung_dan_lembah(perjalanan_hattori)

div = "-------------------------------------------------------------"
print(div)
print("Perjalanan : ", perjalanan_hattori)
print("Jumlah Gunung : ", jumlah_gunung)
print("Jumlah Lembah : ", jumlah_lembah)
print(div)