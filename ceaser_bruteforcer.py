'''
Bruteforce ceaser cipher using python
Author : Abdo
'''
def brute_ceaser(cipher):
    plain = []
    for key in range (26):
        plaintext = ""
        for char in cipher:
            plain_char = ord(char)-key
            if plain_char < ord('a'):
                plain_char = plain_char + 26
            plaintext += chr(plain_char)
        plain.append(plaintext)
    return plain


i = 0
cipher = input("Enter the text : ")
plaintext = brute_ceaser(cipher)
print("==== All the possible plain texts ====")
for plain in plaintext:
    print(i , " : " , plain)
    i = i + 1
