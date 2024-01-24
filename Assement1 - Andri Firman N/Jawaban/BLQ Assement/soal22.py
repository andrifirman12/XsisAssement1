# Panjang awal lilin
panjang_lilin = [3, 3, 9, 6, 7, 8, 23]
deret_fibonacci = [1, 1, 2, 3, 5, 8, 13]


# * Lama Waktu Meleleh masing2 lilin
def lama_meleleh(panjang_awal, laju_meleleh):
    return panjang_awal / laju_meleleh


list_waktu = [
    lama_meleleh(panjang_lilin[i], deret_fibonacci[i])
    for i in range(len(panjang_lilin))
]

# * Cari Waktu Paling Singkat
index_min_waktu = list_waktu.index(
    min(list_waktu)
)
div = "--------------------------------------------------------------------------------"
print(div)
print(f"Index Waktu : {list_waktu}")
print(f"Lilin yang paling pertama habis meleleh adalah lilin ke-{index_min_waktu +1} dengan waktu {list_waktu[index_min_waktu]}")
print(div)