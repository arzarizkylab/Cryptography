import pyperclip

print("--------------------------------------------")
print("PRAKTEK Encryption of Transposition Cipher |")
print("--------------------------------------------")
def main():
    myMessage = 'Arza Rizky Nova Ramadhani'
    myKey = 10
    ciphertext = encryptMessage(myKey, myMessage)
    print("Cipher Text is")
    print(ciphertext)
    pyperclip.copy(ciphertext)
def encryptMessage(key, message):
    ciphertext = [''] * key
    for col in range(key):
        position = col
        while position < len(message):
            ciphertext[col] += message[position]
            position += key
    return ''.join(ciphertext) #Cipher text
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
