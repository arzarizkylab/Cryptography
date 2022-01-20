print("-------------------------------------------")
print("-----------Dekrip & Enkrip Reverse---------")
print("-------------------------------------------")
A = input("Masukan Pesan: ")
f = "" 
h = len(A) - 1
while h >= 0:
    f = f + A[h]
    h = h - 1
print("-------------------------------------------")
print("Hasil Enkripsi: ",f)
print("-------------------------------------------")
B = f
L = "" 
h = len(B) - 1
while h >= 0:
    L = L + B[h]
    h = h - 1
print("Hasil Dekripsi: ",L)
print("-------------------------------------------")
print("-----------Dekrip & Enkrip Caesar----------")
def encrypt(text,key):
	ulangi = ""

	# teks lintas
	for h in range(len(text)):
		karakter = text[h]

		# Enkripsi karakter huruf besar
		if (karakter.isupper()):
			ulangi += chr((ord(karakter) + key - 65) % 26 + 65)

		# Cek Spasi
		elif(karakter.isspace()):
			ulangi += chr((ord(karakter) + key - 32) % 1 + 32)
			

		# Enkripsi karakter huruf kecil
		else:
			ulangi += chr((ord(karakter) + key - 97) % 26 + 97)
	return ulangi
print("-------------------------------------------")
text = input("Masukan Pesan: ")
print("-------------------------------------------")
key = int(input("Masukan key dengan angka: ")) 
print("-------------------------------------------")
print ("Pesan: " + text)
print("-------------------------------------------")
print ("Key: " + str(key))
print("-------------------------------------------")
print ("Hasil Encrypt: " + encrypt(text,key))
hasil_enkripsi = encrypt(text,key)
def decrypt(text,key):
	result = ""

	# teks lintas
	for h in range(len(text)):
		char = text[h]

		# Enkripsi karakter huruf besar
		if (char.isupper()):
			result += chr((ord(char) - key - 65) % 26 + 65)

		# Cek Spasi
		elif(char.isspace()):
			result += chr((ord(char) + key - 32) % 1 + 32)
			

		# Enkripsi karakter huruf kecil
		else:
			result += chr((ord(char) - key - 97) % 26 + 97)
	return result
print("-------------------------------------------")
text = hasil_enkripsi
key = key
print ("Pesan: " + text)
print("-------------------------------------------")
print ("Key: " + str(key))
print("-------------------------------------------")
print ("Hasil Decrypt: " + decrypt(text,key))
print("-------------------------------------------")
print("-----------Dekrip & Enkrip ROT13-----------")

arzarizky = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789',
'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm5678901234')
# Function to translate plain text
def rot13(text):
    return text.translate(arzarizky)
def main():
    txt = input("Masukan Pesan: ")
    print("-------------------------------------------")
    print ("Hasil Enkripsi: ",rot13(txt))
    print("-------------------------------------------")
    hasil = (rot13(txt))
    print ("Hasil Dekripsi: ", rot13(hasil))
    print("-------------------------------------------")
if __name__ == "__main__":
    main()











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
print(color+"31;40m" + h + color + "0m")
print (m)
print (j)
print (n)
print("---------", H, "---------")
print('\x1b[6;30;42m' + X + '\x1b[0m')