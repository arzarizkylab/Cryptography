Pesan = input("Masukan Pesan: ")
Terjemahkan = ""  # teks sandi disimpan dalam variabel ini
i = len(Pesan) - 1
while i >= 0:
    Terjemahkan = Terjemahkan + Pesan[i]
    i = i - 1
print(Terjemahkan)

Flag = Terjemahkan
Hasil = ""  # teks sandi disimpan dalam variabel ini
i = len(Flag) - 1
while i >= 0:
    Hasil = Hasil + Flag[i]
    i = i - 1

print(Hasil)