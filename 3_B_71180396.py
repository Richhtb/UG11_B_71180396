def sisip_kata(kal_awal, kal_sisip, index):
    hasil = kal_awal[:index-1] + kal_sisip + kal_awal[index-1:]
    print(hasil)

kalimat_awal = input('Masukkan kalimat awal: ')
kata_sisip = input('Masukkan kata untuk disisipkan: ')
idx = int(input('Masukkan index: '))
sisip_kata(kalimat_awal, kata_sisip, idx)