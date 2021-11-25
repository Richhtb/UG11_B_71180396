def hitung(kalimat):
    total_huruf = len(kalimat)
    return total_huruf * 2 // 3
kalimat = input('Masukkan kalimat untuk dihitung: ')
print(hitung(kalimat))
