def soal20(jarak_awal, suit_a, suit_b):
    posisi_a = 0
    posisi_b = jarak_awal

    for i in range(len(suit_a)):
        if suit_a[i] == 'G' and suit_b[i] == 'B':
            posisi_a += 2
            posisi_b -= 1
        elif suit_a[i] == 'B' and suit_b[i] == 'K':
            posisi_a += 2
            posisi_b -= 1
        elif suit_a[i] == 'K' and suit_b[i] == 'G':
            posisi_a += 2
            posisi_b -= 1
        elif suit_a[i] == 'B' and suit_b[i] == 'G':
            posisi_a -= 1
            posisi_b += 2
        elif suit_a[i] == 'K' and suit_b[i] == 'B':
            posisi_a -= 1
            posisi_b += 2
        elif suit_a[i] == 'G' and suit_b[i] == 'K':
            posisi_a -= 1
            posisi_b += 2

        if posisi_a >= posisi_b:
            return "A Menang"
        elif posisi_b >= posisi_a:
            return "B Menang"

    return "DRAW"

# Contoh penggunaan
jarak_awal = 2
suit_a = "GGG"
suit_b = "KKB"

pemenang = soal20(jarak_awal, suit_a, suit_b)

div = "--------------------"
print(div)
print(f'''Jarak Awal: {jarak_awal} \nSuit A: {suit_a} \nSuit B: {suit_b}''')
print(f"Hasil: {pemenang}")
print(div)
