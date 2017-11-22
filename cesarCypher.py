alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3
newMessage = ''

# key = input('Enter the encryption key you want to use: ')
# newKey = int(key)
# character = input('Please pick a letter to encrypt: ')
message = input('Please enter a message to encrypt: ')

for character in message:
    position = alphabet.find(character)
    # print(position)
    newPosition = (position + key) % 26
    # print(newPosition)
    newCharacter = alphabet[newPosition]
    print("Encrypted message is: " + newCharacter)
