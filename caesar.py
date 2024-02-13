import sys

#encryp message variable
def encrypt(message, k):
    #create empty variable to store encypted message
    encrypted = ""
    for char in message:
         #shift character by k
         new_char = ord(char) + k
         #wrap around if shift goes past z
         if new_char > ord('z'):
            new_char -= 26
         #convert back to char
         new_message = chr(new_char)
         encrypted += new_message
    return encrypted

#decrypt message variable
def decrypt(message, k):
    #create empty variable to store decrypted message
    decrypted = ""
    for char in message:
         #shift character by k
         new_char = ord(char) - k
         #wrap around if shift goes past a
         if new_char < ord('a'):
            new_char += 26
         # Convert back to char 
         ori_message = chr(new_char)
         decrypted += ori_message
    return decrypted


if __name__ == "__main__":
    #take in first arg as word
    message = sys.argv[1]
    #take in second arg as int key
    key = int(sys.argv[2])

#encrypt your word
encrypted = encrypt(message, key)

#decrypt your encrypted word
decrypted = decrypt(encrypted, key)

print("Your encrypted word is", encrypted)
print("Your decrypted word is", decrypted)