# Let's look at the lowercase letters.
import string
string.ascii_lowercase

# We will consider the alphabet to be these letters, along with a space.
alphabet = string.ascii_lowercase + " "

# create `letters` here!
letters = {}
for i in range(0,27):
    letters[i] = alphabet[i]