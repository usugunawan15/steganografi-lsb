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