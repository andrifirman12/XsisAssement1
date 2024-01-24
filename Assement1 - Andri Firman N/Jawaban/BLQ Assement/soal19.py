def adalah_pangram(kalimat):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    kalimat_lower = kalimat.lower()
    pangram = True

    for x in alphabet:
        if x not in kalimat_lower:
            pangram = False
    
    if pangram == True:
        print("'" + kalimat + "' = Pangram" )
    else:
        print("'" + kalimat + "' = Bukan Pangram" )

kalimat1 = "Sphinx of black quartz, judge my vow"
kalimat2 = "Brawny gods just flocked up to quiz and vex him"
kalimat3 = "Check back tomorrow; I will see if the book has arrived."
div = "--------------------------------------------------------------------------------"

print(div)
adalah_pangram(kalimat1)
adalah_pangram(kalimat2)
adalah_pangram(kalimat3)
print(div)
