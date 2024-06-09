letters='abcdefghijklmnopqrstuvwxyz'
def encDec(text,mode,key): #a function that integrates both the encrypt & decrypt function to avoid repeated code
    result=''
    if mode=='d':
        key=-key

    for letter in text:
        letter=letter.lower()
        if not letter=='':
            index=letters.find(letter)
            if index==-1:
                result+=letter
            else:
                uindex=index+key
                if uindex>=26:
                    uindex-=26
                elif uindex<0:
                    uindex+=26
                result+=letters[uindex]
    return result

print(" C A E S E R  C I P H E R  P R O G R A M")
print()
print("do you want to encrypt (press e) or decrypt(press d)?")
choice=input('e/d:').lower()
print()
if choice=='e':
    print('MODE SELECTED : ENCRYPTION')
    key=int(input('please provide key:'))
    message=input('enter message:')
    ciphertext=encDec(message,choice,key)
    print(f'CIPHERTEXT:{ciphertext}')

elif choice=='d':
    print('MODE SELECTED : DECRYPTION')
    key=int(input('please provide key:'))
    message=input('enter message:')
    plaintext=encDec(message,choice,key)
    print(f'PLAINTEXT:{plaintext}')

'''def encrypt(plaintext,key):
    ciphertext=''
    for letter in plaintext:
        letter=letter.lower()   
        if not letter==' ':
            index=letters.find(letter)
            if index==-1:
                ciphertext+=letter    
            else:
                uindex=index+key  
                if uindex<0:       
                    uindex+=26
                ciphertext+=letters[uindex]
    return ciphertext
def decrypt(ciphertext,key):
    plaintext=''
    for letter in ciphertext:
        letter=letter.lower()   
        if not letter==' ':
            index=letters.find(letter)
            if index==-1:
                plaintext+=letter   
            else:
                uindex=index-key  
                if uindex>=26:       
                    uindex-=26
                plaintext+=letters[uindex]
    return plaintext'''


