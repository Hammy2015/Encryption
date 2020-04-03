def Encrypt(toEncrypt):
    if toEncrypt == 'a':
        return toEncrypt.replace('a', 'z')
    if toEncrypt == 'b':
        return toEncrypt.replace('b', 'y')
    if toEncrypt == 'c':
        return toEncrypt.replace('c', 'x')
    if toEncrypt == 'd':
        return toEncrypt.replace('d', 'w')
    if toEncrypt == 'e':
        return toEncrypt.replace('e', 'v')
    if toEncrypt == 'f':
        return toEncrypt.replace('f', 'u')
    if toEncrypt == 'g':
        return toEncrypt.replace('g', 't')
    if toEncrypt == 'h':
        return toEncrypt.replace('h', 's')
    if toEncrypt == 'i':
        return toEncrypt.replace('i', 'r')
    if toEncrypt == 'j':
        return toEncrypt.replace('j', 'q')
    if toEncrypt == 'k':
        return toEncrypt.replace('k', 'p')
    if toEncrypt == 'l':
        return toEncrypt.replace('l', 'o')
    if toEncrypt == 'm':
        return toEncrypt.replace('m', 'n')
    if toEncrypt == 'n':
        return toEncrypt.replace('n', 'm')
    if toEncrypt == 'o':
        return toEncrypt.replace('o', 'l')
    if toEncrypt == 'p':
        return toEncrypt.replace('p', 'k')
    if toEncrypt == 'q':
        return toEncrypt.replace('q', 'j')
    if toEncrypt == 'r':
        return toEncrypt.replace('r', 'i')
    if toEncrypt == 's':
        return toEncrypt.replace('s', 'h')
    if toEncrypt == 't':
        return toEncrypt.replace('t', 'g')
    if toEncrypt == 'u':
        return toEncrypt.replace('u', 'f')
    if toEncrypt == 'v':
        return toEncrypt.replace('v', 'e')
    if toEncrypt == 'w':
        return toEncrypt.replace('w', 'd')
    if toEncrypt == 'x':
        return toEncrypt.replace('x', 'c')
    if toEncrypt == 'y':
        return toEncrypt.replace('y', 'b')
    return toEncrypt.replace('z', 'a')


repeat = 1
while repeat == 1:
    toEncrypt = input("What do you want to encode code?: ")

    i = 0
    r = ''

    while i < len(toEncrypt):
        r = r + Encrypt(toEncrypt[i])
        i = i + 1
    print(r)
    repeat = int(input("Code another?(1=yes):"))
