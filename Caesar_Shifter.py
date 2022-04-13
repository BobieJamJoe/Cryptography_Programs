keyChange = 0

while True:
    pass
    key = input("Input shift key: ")
    if key.lower() == "quit":
        quit()
    keyChange = 0

    while keyChange == 0:
        letter = input("Input letter to shift: ")
        if letter.lower() == "change key":
            keyChange = 1
        elif letter.lower() == "quit":
            quit()

        alphabetLower = "abcdefghijklmnopqrstuvwxyz"
        alphabetUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "1234567890"
        n = -1
        x = -1

        for i in alphabetLower:
            n += 1
            if i == letter:
                print(alphabetLower[(n + int(key)) % 26])
            elif i.upper() == letter:
                print(alphabetUpper[(n + int(key)) % 26])

        for i in numbers:
            x += 1
            if i == letter:
                print(numbers[(x + int(key)) % 10])
