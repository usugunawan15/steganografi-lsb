------------------------
|| Caesar Chipper 1.0 ||
------------------------

print("Pilih mode:")
print("1 encrypt")
print("2 decrypt")
mode = int(input())
print("Masukkan key yang dipilih (0 hingga 25):")
key = int(input())
print("Masukkan pesan:")
message = input()
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
translated = ''
message = message.upper()
for symbol in message:
    if symbol in letters:
        num = letters.find(symbol)
        if mode <= 1:
            num += key
        elif mode >= 2:
            num -= key
        if num >= len(letters):
            num -= len(letters)
        elif num < 0:
            num += len(letters)
        translated += letters[num]
    else:
        translated += symbol
print(translated)


------------------------
|| Caesar Chipper 2.0 ||
------------------------

import string
abjad = string.printable

def enkrip (pesan):
    global abjad

    key = int (input ('Masukkan key : '))
    cipher= ''
    for i in pesan :
        if i in abjad:
            k = abjad.find(i)
            k = (k+key)%100
            cipher = cipher + abjad[k]
        else:
            cipher = cipher + i

    return cipher

def dekrip (cipher):
    global abjad

    key = int (input ('Masukkan key : '))
    pesan= ''
    for i in cipher :
        if i in abjad:
            k = abjad.find(i)
            k = (k-key)%100
            pesan = pesan + abjad[k]
        else:
            pesan = pesan + i

    return pesan

if __name__ == '__main__':
    print('---------------------')
    print('---------------------')
    print('By : Kelompok 5')
    print('Afnan, Usu, M. Rafiqi')
    print('---------------------')
    print('---------------------')
    pilihan = int (input ('1. Enkripsi\n2. Dekripsi\n----------\nPilih mode :'))

   
    if pilihan == 1:
        pesan = input ('Masukkan pesan (Plaintext) : ')
        print (enkrip(pesan))
    elif pilihan ==2:
        cipher = input ('Masukkan pesan (CipherText) : ')
        print (dekrip(cipher))
    else:
        print ('Masukkan pilihan 1 atau 2 !!')
