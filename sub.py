f = open("4", "r")

email = f.readline()

decrypt = ""
for letter in email:
    if letter == 'e':
        decrypt = decrypt + 'e'
    if letter == 'x':
        decrypt = decrypt + 'o'
    if letter == 'u':
        decrypt = decrypt + 't'
    if letter == 'y':
        decrypt = decrypt + 'a'
    if letter == 's':
        decrypt = decrypt + 's'
    if letter == 'b':
        decrypt = decrypt + 'n'
    if letter == 'g':
        decrypt = decrypt + 'i'
    if letter == 'l':
        decrypt = decrypt + 'h'
    if letter == 'a':
        decrypt = decrypt + 'r'
    if letter == 'q':
        decrypt = decrypt + 'd'
    if letter == 'w':
        decrypt = decrypt + 'w'
    if letter == 'k':
        decrypt = decrypt + 'u'
    if letter == 'v':
        decrypt = decrypt + 'l'
    if letter == 'd':
        decrypt = decrypt + 'm'
    if letter == 'p':
        decrypt = decrypt + 'g'
    if letter == 'h':
        decrypt = decrypt + 'y'
    if letter == 'o':
        decrypt = decrypt + 'b'
    if letter == 'm':
        decrypt = decrypt + 'f'
    if letter == 'i':
        decrypt = decrypt + 'v'
    if letter == 'j':
        decrypt = decrypt + 'p'
    if letter == 'z':
        decrypt = decrypt + 'c'
    if letter == 'r':
        decrypt = decrypt + 'k'
    if letter == 'n':
        decrypt = decrypt + 'j'
    if letter == 'f':
        decrypt = decrypt + 'q'
print(decrypt)
