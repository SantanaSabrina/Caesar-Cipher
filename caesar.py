import sys

message = "hello world"
k = 10

def encrypt(message, k):
    encrypted = ""
    for char in encrypted:
         #shift character by k
         new_char = ord(char) + k
         #convert back to char
         new_message = chr(new_char)
         encrypted += new_message
    return encrypt(message, key)


def decrypt(message, k):
   decrypted = ""
   for char in decrypted:
         #shift character by k
         new_char = ord(char) - k
         #convert back to char 
         ori_message = chr(new_char)
         decrypted += ori_message
   return decrypt(message, key)


if __name__ == "__main__":
    # take in first arg as word
    message = sys.argv[1]
    # take in second arg as int key
    key = int(sys.argv[2])

    # encrypt your word
    encrypted = encrypt(message, key)

    # decrypt your encrypted word
    decrypted = decrypt(encrypted, key)

    print("Your encrypted word is", encrypted)
    print("Your decrypted word is", decrypted)
