# Program Python untuk diimplementasikan
# ROT13 Caesar cipher
 
'''Skrip ini menggunakan kamus 'chr()' & 'ord()' fungsi'''
 
# Kamus untuk mencari indeks abjad
dict1 = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5,
        'F' : 6, 'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10,
        'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14, 'O' : 15,
        'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20,
        'U' : 21, 'V' : 22, 'W' : 23, 'X' : 24, 'Y' : 25, 'Z' : 26 }
 
# Kamus untuk mencari abjad
# sesuai dengan indeks setelah shift
dict2 = {0 : 'Z', 1 : 'A', 2 : 'B', 3 : 'C', 4 : 'D', 5 : 'E',
        6 : 'F', 7 : 'G', 8 : 'H', 9 : 'I', 10 : 'J',
        11 : 'K', 12 : 'L', 13 : 'M', 14 : 'N', 15 : 'O',
        16 : 'P', 17 : 'Q', 18 : 'R', 19 : 'S', 20 : 'T',
        21 : 'U', 22 : 'V', 23 : 'W', 24 : 'X', 25 : 'Y'}
 

# Berfungsi untuk mengenkripsi string
#sesuai shift yang disediakan
def encrypt(message, shift):
    cipher = ''
    for letter in message:
        # memeriksa ruang
        if(letter != ' '):
            # mencari kamus dan
            # menambahkan pergeseran ke indeks
            num = ( dict1[letter] + shift ) % 26
            # looks up the second dictionary for
            # the shifted alphabets and adds them
            cipher += dict2[num]
        else:
            # adds space
            cipher += ' '
 
    return cipher
 
# Berfungsi untuk mendekripsi string
#sesuai shift yang disediakan
def decrypt(message, shift):
    decipher = ''
    for letter in message:
        # checks for space
        if(letter != ' '):
            # looks up the dictionary and
            # subtracts the shift to the index
            num = ( dict1[letter] - shift + 26) % 26
            # looks up the second dictionary for the
            # shifted alphabets and adds them
            decipher += dict2[num]
        else:
            # adds space
            decipher += ' '
 
    return decipher
print("-------------------------------------------")
print("PRAKTEK ROT 13 Algorithm                  |")
print("-------------------------------------------")
# fungsi driver untuk menjalankan program
def main():
    # gunakan fungsi 'upper()' untuk mengubah karakter huruf kecil menjadi huruf besar
    message = input("Masukan Pesan: ")
    shift = 14 # disini saya menggunakn shift 14 ini sesuai keinginan 
               # sebenarnya menggunakan shift 13 agar sesuai judulnya
               # tapi saya pakai 14 biar beda sama yang lain hehehe  
    result = encrypt(message.upper(), shift)
    print ("Input                : ", message)
    print ("Hasil Output Enkripsi: ",result)
    print("-------------------------------------------")
    message = result
    shift = 14 # disini saya menggunakn shift 14 ini sesuai keinginan 
               # sebenarnya menggunakan shift 13 agar sesuai judulnya
               # tapi saya pakai 14 biar beda sama yang lain hehehe  
    result = decrypt(message.upper(), shift)
    print ("Input                : ", message)
    print ("Hasil Output Dekripsi: ",result)
 
# Menjalankan fungsi utama
if __name__ == '__main__':
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
print("-------------------------------------------")
print(color+"31;40m" + h + color + "0m")
print (m)
print (j)
print (n)
print("---------", H, "---------")
print('\x1b[6;30;42m' + X + '\x1b[0m')