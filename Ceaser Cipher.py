'''
Encrypting and decrypting using ceaser cipher
Author : Abdo
'''

alph = "abcdefghijklmnopqrstuvwxyz"

def encr (plain,key) : #encrypting block
    plain = plain.lower()
    cipher = ""
    for state in plain :
        #condition for special character
        if state not in alph :
            cipher += state
        else :
            cipher += alph[ ( alph.index(state) + key ) % 25   ]
    return cipher

def decr (cipher,key) : #decrypting block
    cipher = cipher.lower()
    plain = ""
    for state in cipher :
        #condition for special character
        if state not in alph :
            cipher += state
        else :
            plain += alph[ ( alph.index(state) - key ) %25 ]
    return plain

text = input("Encrypt or Decrypt : ")
text = text.lower()
x = str(input("Enter the word : "))
y = int(input("Enter the key : "))

if text == "encrypt" :
    print(encr(x,y))
elif text == "decrypt" :
    print(decr(x,y))
else : print("Wrong input")

Enter  = input("Enter to End")
