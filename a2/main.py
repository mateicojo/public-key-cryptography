def bellaso_encrypt(message, key):
    alph=" ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key=key.upper()
    message = message.upper()
    overlay=""
    inner_index=0
    encrypted=""
    for i in range(len(message)):
        if inner_index > len(key)-1:
            inner_index=0
        overlay=overlay + key[inner_index]
        inner_index+=1
        #print(overlay)
    for i in range(len(message)):
        if(not message[i].isalpha() and message[i]!=" "):
            encrypted+=message[i]
        else:
            encrypted= encrypted + shift_letter(message[i],get_index_of_letter(overlay[i]))
    return encrypted

def get_index_of_letter(letter):
    return ord(letter)-ord('A')

def shift_letter(letter, offset):
    new_index = (ord(letter) - ord('A') + offset) % 26
    return chr(new_index+ord('A'))

print(bellaso_encrypt("Ana are mere", "Key"))
