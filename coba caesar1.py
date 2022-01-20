def encrypt(text,s):
	result = ""

	# teks lintas
	for i in range(len(text)):
		char = text[i]

		# Enkripsi karakter huruf besar
		if (char.isupper()):
			result += chr((ord(char) + s-65) % 26 + 65)

		# Cek Spasi
		elif(char.isspace()):
			result += chr((ord(char) + s-32) % 1 + 32)
			

		# Enkripsi karakter huruf kecil
		else:
			result += chr((ord(char) + s - 97) % 26 + 97)

	return result
text = "CD CD cd"
s = 1 
print ("Text    : " + text)
print ("Shift   : " + str(s))
print ("Cipher  : " + encrypt(text,s))