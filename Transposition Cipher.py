def split_len(seq, length):
    return [seq[i:i + length] for i in range(0, len(seq), length)]
def encode(key, plaintext):
    order = {
        int(val): num for num, val in enumerate(key)
    }
    ciphertext = ''
    for index in sorted(order.keys()):
        for part in split_len(plaintext, len(key)):
            try:
                ciphertext += part[order[index]]
            except IndexError:
                continue
    return ciphertext
print("---------------------")
print("Hasil Sesuai Contoh |")
print("---------------------")
print(encode('3214', 'HELLO'))

# Implementasi Python3 dari
# Transposisi Kolom
import math
from termcolor import colored
print("---------------------")
key = input("Masukan KEY Kawan: ")
error_geng_gabisa = colored('Program ini tidak dapat menangani pengulangan huruf pada KEY.', 'green')
# Enkripsi
def encryptMessage(msg):
	cipher = ""

	# lacak indeks kunci
	k_indx = 0

	msg_len = float(len(msg))
	msg_lst = list(msg)
	key_lst = sorted(list(key))

	# menghitung kolom matriks
	col = len(key)
	
	# hitung baris maksimum matriks
	row = int(math.ceil(msg_len / col))

	# tambahkan karakter padding '_' di tempat kosong
	# sel matix yang kosong
	fill_null = int((row * col) - msg_len)
	msg_lst.extend('_' * fill_null)

	# buat Matriks dan masukkan pesan dan
	# karakter bantalan baris-bijaksana
	matrix = [msg_lst[i: i + col]
			for i in range(0, len(msg_lst), col)]

	# baca matriks kolom-bijaksana menggunakan kunci
	for _ in range(col):
		curr_idx = key.index(key_lst[k_indx])
		cipher += ''.join([row[curr_idx]
						for row in matrix])
		k_indx += 1

	return cipher

# Dekripsi
def decryptMessage(cipher):
	msg = ""

	# lacak indeks kunci
	k_indx = 0

	# lacak indeks pesan
	msg_indx = 0
	msg_len = float(len(cipher))
	msg_lst = list(cipher)

	# menghitung kolom matriks
	col = len(key)
	
	# hitung baris maksimum matriks
	row = int(math.ceil(msg_len / col))

	# ubah kunci menjadi daftar dan urutkan
	# menurut abjad sehingga kami dapat mengakses
	# setiap karakter berdasarkan posisi abjadnya.
	key_lst = sorted(list(key))

	# buat matriks kosong untuk
	# simpan pesan yang diuraikan
	dec_cipher = []
	for _ in range(row):
		dec_cipher += [[None] * col]

	# Susunlah kolom matriks sesuai
	# ke urutan permutasi dengan menambahkan ke matriks baru
	for _ in range(col):
		curr_idx = key.index(key_lst[k_indx])

		for j in range(row):
			dec_cipher[j][curr_idx] = msg_lst[msg_indx]
			msg_indx += 1
		k_indx += 1

	# ubah matriks pesan terdekripsi menjadi string
	try:
		msg = ''.join(sum(dec_cipher, []))
	except:
		raise TypeError(error_geng_gabisa)

	null_count = msg.count('_')

	if null_count > 0:
		return msg[: -null_count]

	return msg

# Kode Pengemudi
print("-------------------------------------")
print("Hasil Coba Cipher Transposisi Kolom |")
print("-------------------------------------")
msg = "Arza Rizky Nova Ramadhani"

cipher = encryptMessage(msg)
print("Output Enkripsi = {}".
			format(cipher))

print("Output Dekrip   = {}".
	format(decryptMessage(cipher)))



# Program Python3 untuk diilustrasikan
# Rail Fence Cipher

# berfungsi untuk mengenkripsi pesan
def encryptRailFence(text, key):

	# buat matriks ke cipher
	# kunci teks biasa = baris ,
	# panjang(teks) = kolom
	# mengisi matriks rel
	# untuk membedakan diisi
	# spasi dari yang kosongs
	rail = [['\n' for i in range(len(text))]
				for j in range(key)]
	
	#menemukan arah
	dir_down = False
	row, col = 0, 0
	
	for i in range(len(text)):
		
		# periksa arah aliran
		# membalikkan arah jika kita baru saja
		# mengisi rel atas atau bawah
		if (row == 0) or (row == key - 1):
			dir_down = not dir_down
		
		# isi alfabet yang sesuai
		rail[row][col] = text[i]
		col += 1
		
		# temukan baris berikutnya menggunakan
		# bendera arah
		if dir_down:
			row += 1
		else:
			row -= 1
	# sekarang kita bisa membuat sandinya
	# menggunakan matriks rel
	result = []
	for i in range(key):
		for j in range(len(text)):
			if rail[i][j] != '\n':
				result.append(rail[i][j])
	return("" . join(result))
	
# Fungsi ini menerima teks sandi
# dan kunci dan kembalikan yang asli
# teks setelah dekripsi
def decryptRailFence(cipher, key):

	# buat matriks ke cipher
	# kunci teks biasa = baris ,
	# panjang(teks) = kolom
	# mengisi matriks rel ke
	# membedakan ruang yang terisi
	# dari yang kosong
	rail = [['\n' for i in range(len(cipher))]
				for j in range(key)]
	
	# menemukan arah
	dir_down = None
	row, col = 0, 0
	
	# mark the places with '*'
	for i in range(len(cipher)):
		if row == 0:
			dir_down = True
		if row == key - 1:
			dir_down = False
		
		# letakkan penanda
		rail[row][col] = '*'
		col += 1
		
		# temukan baris berikutnya
		# menggunakan bendera arah
		if dir_down:
			row += 1
		else:
			row -= 1
			
	# sekarang kita bisa membangun
	# isi matriks rel
	index = 0
	for i in range(key):
		for j in range(len(cipher)):
			if ((rail[i][j] == '*') and
			(index < len(cipher))):
				rail[i][j] = cipher[index]
				index += 1
		
	# sekarang baca matriks di
	# cara zig-zag untuk membangun
	# teks yang dihasilkan
	result = []
	row, col = 0, 0
	for i in range(len(cipher)):
		
		# periksa arah aliran
		if row == 0:
			dir_down = True
		if row == key-1:
			dir_down = False
			
		# letakkan penanda
		if (rail[row][col] != '*'):
			result.append(rail[row][col])
			col += 1
			
		# temukan baris berikutnya menggunakan
		# bendera arah
		if dir_down:
			row += 1
		else:
			row -= 1
	return("".join(result))

print("-------------------------------------")
print("Hasil Coba Rail Fence Cipher 	   |")
print("-------------------------------------")
# Kode pengemudi
if __name__ == "__main__":
	input1 = "Arza Rizky Nova Ramadhani"
	hasil1 = (encryptRailFence(input1, 2)) 
	hasil2 = (encryptRailFence(input1, 3))
	hasil3 = (encryptRailFence(input1, 4))
	print("Output Enkripsi = ", encryptRailFence(hasil1, 2))
	print("Output Enkripsi = ", encryptRailFence(hasil2, 3))
	print("Output Enkripsi = ", encryptRailFence(hasil3, 4))
	
	# Sekarang dekripsi
	# cipher-teks yang sama
	print("Output Dekrip   = ", decryptRailFence(hasil1, 2))
	print("Output Dekrip   = ", decryptRailFence(hasil2, 3))
	print("Output Dekrip   = ", decryptRailFence(hasil3, 4))
g = " :       amaN"
f = "" 
i = len(g) - 1
while i >= 0:
    f = f + g[i]
    i = i - 1
a = "inahdamaR avoN ykziR azrA"
m = f
i = len(a) - 1
while i >= 0:
    m = m + a[i]
    i = i - 1
p = " :      saleK"
q = "" 
i = len(p) - 1
while i >= 0:
    q = q + p[i]
    i = i - 1
k = "4TIIX"
j = q
i = len(k) - 1
while i >= 0:
    j = j + k[i]
    i = i - 1
A = " :   nesbA oN"
B = "" 
i = len(A) - 1
while i >= 0:
    B = B + A[i]
    i = i - 1
h = "60"
n = B
i = len(h) - 1
while i >= 0:
    n = n + h[i]
    i = i - 1
b = "helO nakajrekiD"
h = "" 
i = len(b) - 1
while i >= 0:
    h = h + b[i]
    i = i - 1
B = "aboyn hadu iisakaM"
H = "" 
i = len(B) - 1
while i >= 0:
    H = H + B[i]
    i = i - 1
G = "!sseccuS"
X = "" 
i = len(G) - 1
while i >= 0:
    X = X + G[i]
    i = i - 1
color = "\x1B["
print("-------------------------------------")
print(color+"31;40m" + h + color + "0m")
print (m)
print (j)
print (n)
print("---------", H, "---------")
print('\x1b[6;30;42m' + X + '\x1b[0m')