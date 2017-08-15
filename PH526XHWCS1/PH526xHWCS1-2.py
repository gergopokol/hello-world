alphabet = string.ascii_lowercase + " "
letters = dict(enumerate(alphabet))

encryption_key = 3

encoding = {}
for i in range(0,27):
    encoding[alphabet[i]] = (i + encryption_key) %27

