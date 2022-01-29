import string
from tracemalloc import stop

def dekripsi():
    print('1. Decrypt positif')
    print('2. Decrypt negatif')
    choose = input('silahkan pilih (1/2) : ')
    if choose == '1':
        print("Choose your method: ")
        print("1. ASCII")
        print("2. Cipher")
        choise = input('enter your method: ')
        if choise == '1':
            Message = input('Input your ASCII: ')
            decodedmessage = ""
            for item in Message.split():
                decodedmessage += chr(int(item))
            plaintext = decodedmessage
            def caesar(char, key):
                output_text = ""
                for i in range(len(plaintext)):
                    char = plaintext[i]
                    if (char.isupper()):
                        output_text += chr((ord(char) - key - 65) % 26 + 65)      
                    elif (char.isnumeric()):
                        output_text += chr((ord(char) - key - 48) % 10 + 48)
                    elif (char.islower()):
                        output_text += chr((ord(char) - key - 97) % 26 + 97)    
                    else:
                        output_text += chr((ord(char) - key - 32) % 15 + 32)
                return output_text
            file = open("Output bruteforce.txt", "r+")
            file.write("Berikut Adalah Hasil BruteForce : " + plaintext)
            for key in range(26):
                hasil = ('using key: ' + str(key) , str(caesar(plaintext, key)))
                file.write("\n")
                file.write(str(hasil))
            file.close()
            x = input('Want Another BruteForce? (y/n) : ')
            while x == "y":
                start()
            else:
                print("Dymi Kavindra XII TKJ 2 / 13")
                quit()
        if choise == '2':
            plaintext = input("Input your Cipher : ")
            def caesar(char, key):
                output_text = ""
                for i in range(len(plaintext)):
                    char = plaintext[i]
                    if (char.isupper()):
                        output_text += chr((ord(char) - key - 65) % 26 + 65)      
                    elif (char.isnumeric()):
                        output_text += chr((ord(char) - key - 48) % 10 + 48)
                    elif (char.islower()):
                        output_text += chr((ord(char) - key - 97) % 26 + 97)    
                    else:
                        output_text += chr((ord(char) - key - 32) % 15 + 32)
                return output_text
            file = open("Output bruteforce.txt", "r+")
            file.write("Berikut Adalah Hasil BruteForce : " + plaintext)
            for key in range(26):
                    hasil = ('using key: ' + str(key) , str(caesar(plaintext, key)))
                    file.write("\n")
                    file.write(str(hasil))
            file.close()
            x = input('Want Another BruteForce? (y/n) : ')
            while x == "y":
                start()
            else:
                print("Dymi Kavindra XII TKJ 2 / 13")
                quit()
                
    elif choose == '2':
        print("Choose your method: ")
        print("1. ASCII")
        print("2. Cipher")
        pilih = input('enter your method: ')
        if pilih == '1':
            pesan = input("Input your ASCII: ")
            decodedmessage = ""
            for item in pesan.split():
                decodedmessage += chr(int(item))
            encrypted = decodedmessage
            def decrypt(char, key):
                output_text = ""
                for i in range(len(encrypted)):
                    char = encrypted[i]
                    if (char.isupper()):
                        output_text += chr((ord(char) + key - 65) % 26 + 65)
                        if (char.isupper()) > 90:
                            char = char -26        
                    elif (char.isnumeric()):
                        output_text += chr((ord(char) + key - 48) % 10 + 48)
                        if (char.isnumeric()) > 57:
                            char = char - 10
                    elif (char.islower()):
                        output_text += chr((ord(char) + key - 97) % 26 + 97)
                        if (char.islower()) > 122:
                            char = char - 26
                    else:
                        output_text += chr((ord(char) + key - 32) % 15 + 32)
                return output_text
            file = open("Output bruteforce.txt", "r+")
            file.write("Berikut Adalah Hasil BruteForce KODE ASCII : " + encrypted)
            for key in range(26):
                    result = ("using key: -" + str(key) , decrypt(encrypted, key))
                    file.write("\n")
                    file.write(str(result))
            file.close()
            x = input('Want Another BruteForce? (y/n) : ')
            while x == "y":
                start()
            else:
                print("Dymi Kavindra XII TKJ 2 / 13")
                quit()
        elif pilih == '2':
            cipher = input("Input your Ciphertext : ")
            def decrypt(char, key):
                output_text = ""
                for i in range(len(cipher)):
                    char = cipher[i]
                    if (char.isupper()):
                        output_text += chr((ord(char) + key - 65) % 26 + 65)
                        if (char.isupper()) > 90:
                            char = char -26        
                    elif (char.isnumeric()):
                        output_text += chr((ord(char) + key - 48) % 10 + 48)
                        if (char.isnumeric()) > 57:
                            char = char - 10
                    elif (char.islower()):
                        output_text += chr((ord(char) + key - 97) % 26 + 97)
                        if (char.islower()) > 122:
                            char = char - 26
                    else:
                        output_text += chr((ord(char) + key - 32) % 15 + 32)
                return output_text
            file = open("Output bruteforce.txt", "r+")
            file.write("Berikut Adalah Hasil BruteForce : " + cipher)
            for key in range(26):
                    result = ("using key: -" + str(key) , decrypt(cipher, key))
                    file.write("\n")
                    file.write(str(result))
            file.close()
            x = input('Want Another BruteForce? (y/n) : ')
            if x == "y":
                start()
            else:
                print("Dymi Kavindra XII TKJ 2 / 13")
                quit()
        else:
            print("Invalid input")
def start():
    v = input("PRESS ENTER TO START...")
    if v == '':
        print("starting program...")
        dekripsi()
    else:
        stop()
        
print("Welcoem to the program")
c = input("You want to start (y/n) : ")        
if c == 'y':
    start()
else:
    print("ok")
    stop()

