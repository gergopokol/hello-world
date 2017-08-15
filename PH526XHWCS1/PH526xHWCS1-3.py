message = "hi my name is caesar"

def caesar(message, encryption_key):
    # return the encoded message as a single string!
    encoding = {}
    for i in range(0,27):
        encoding[alphabet[i]] = (i + encryption_key) %27
    encoded_message = ""
    for char in message:
        encoded_message += letters[encoding[char]]
    return encoded_message

encoded_message = caesar(message,3)
print(encoded_message)