def getMessage():
    print('Enter your message:')
    return input()
def encrypt(text,key):
    result = ''
    for i in range(len(text)):
        char = text[i] 
        if (char.isupper()):
            result += chr((ord(char) + key - 65) % 26 + 65)
        elif(char.isnumeric()):
            result += chr((ord(char) + key - 48) % 10 + 48)
        elif (char.islower()):
            result += chr((ord(char) + key - 97) % 26 + 97)
        elif (ord(char)) >= 32 and ord(char) <= 47:
            result += chr((ord(char) + key - 32) % 15 + 32) #contoh menggunakan lebih dan kurang
        else:
            result += chr((ord(char) + key - 48) % 10 + 48)
    return result
text = getMessage()
s = int(input('ur shift?: '))
print ("Plain Text : " + text)
print ("Shift pattern : " + str(s))
print ("Cipher: " + encrypt(text,s))
convert = input('conver to ASCII? (y/n) ')
if convert == 'y':
    value = encrypt(text,s)
    list=[ord(ch) for ch in value]
    ascii= ''.join(str(list).split(','))
    print(ascii)
else:
    print('thanks!')

