######################### Encrypt and Decrypt functions #########################
def encrypt():
    P = int(input("Enter P value (must be prime): "))
    Q = int(input("Enter Q value (must be prime): "))
    n = P * Q
    phiN = (P - 1)*(Q - 1)
    e = int(input("Enter e value (1 < e < phiN): "))
    d = pow(e, -1, phiN)
    print("Your public key is: (n = " + str(n) + ", e = " + str(e) + ")")
    print("Your private key is: (n = " + str(n) + ", d = " + str(d) + ")")

    while True:
        m = input("Message to encrypt: ")
        # Encodes message to bytes, then converts to hex format, then base16 integer
        m_int = int(m.encode().hex(), 16)

        # Key size detector
        if len(str(m_int)) >= len(str(n)):
            print("Message is too long. Try again.")

        elif len(str(m_int)) < len(str(n)):
            c = pow(m_int, e, n)
            print("Your encryptd message is (" + str(c) + ") Use your private key to decrypt it")
            break


def decrypt():
    d = int(input("Enter d value: "))
    n = int(input("Enter n value: "))
    c = int(input("Enter ciphertext (must be integer): "))
    m = pow(c, d, n)
    decode = input("Print result or decode from hex? (p for print, d for decode): ")

    if decode == "p":
        print("Your decrypted message is (" + str(m) + ") Use a decoder to convert to text")

    elif decode == "d":
        print(bytes.fromhex(hex(m)[2:]).decode())

    else:
        print("Invalid option. Printing result")
        print("Your decrypted message is (" + str(m) + ") Use a decryptr to convert to text")
###############################################################################

eORd = input("Would you like to encrypt or decrypt? (e for encrypt, d for decrypt): ")


if eORd == "e":
    encrypt()


elif eORd == "d":
    decrypt()


else:
    print("Invalid option. Quitting the program")
    quit()
