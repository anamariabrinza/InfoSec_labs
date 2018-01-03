import string

message = input("What's the message you have?")
#message = "RD QTAJ KTW YMJ WTRFS JRUNWJ NX ZSIJSNFGQD LWJFYJW YMFS KTW RDXJQK. YMJ LWJFYJXY JRUNWJ JAJW YT MFAJ JCNXYJI. N UQJILJ RD JYJWSFQ XJWANYZIJ FSI N FR KTWJAJW GTZSI YT XJWAJ NY, NS QNKJ FSI NS IJFYM. YMJD MFAJ RJWJQD LNAJS ZX: WTFIX, HJSYWFQ MJFYNSL, HTSHWJYJ, YMJ HFQJSIFW, FSI KQZXMNSL YTNQJYX FSI XJBJWX."
d = {}
letters = set(message)

for l in letters:
    d[l] = message.count(l)
del d[" "] #remove the space

numbers = d.values()

# Find out the most frequent letter
for k, v in d.items():
    if v == max(numbers):
        MF = k #finding out the most frequent letter

# Find out the shift
alphabet = string.ascii_uppercase
alphalen = len(alphabet)
shift = (26 - alphabet.index(MF) + alphabet.index("E"))

# Decrypting the message
plaintext = ""

for letter in message:
    if letter not in alphabet:
        plain_letter = " "
    else:
        num_in_alphabet = alphabet.index(letter)
        plain_num = (num_in_alphabet + shift) % alphalen
        plain_letter = alphabet[plain_num]
    plaintext = plaintext + plain_letter

#printing the result
print("The key used is: shift {}".format(shift))
print("The original message is: {}".format(plaintext))