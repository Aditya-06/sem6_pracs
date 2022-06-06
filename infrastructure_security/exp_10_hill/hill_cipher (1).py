def text_to_digits(text):
    result = []
    for i in range(len(text)):
        char = text[i]
        if char == " ":
            result.append("27")
        elif char.isupper():
            result.append(ord(char) % 65)
        else:
            result.append(ord(char) % 97)
    return result


def digits_to_text(digits):
    result = []
    for i in range(len(digits)):
        char = digits[i]
        if char == "27":
            result.append(" ")
        else:
            result.append(chr(char + 65))
    return result


def get_key_matrix(key, n):
    keyMatrix = [[0] * n for i in range(n)]
    k = 0
    for i in range(n):
        for j in range(n):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1

    return keyMatrix


def encrypt(text, key):
    n = len(text)
    key_matrix = get_key_matrix(key, n)

    digits = text_to_digits(text)

    column_matrix = [[0] for i in range(n)]

    for i in range(n):
        column_matrix[i][0] = digits[i]

    cipher_matrix = [[0] for i in range(n)]

    for i in range(n):
        for j in range(1):
            cipher_matrix[i][j] = 0
            for x in range(n):
                cipher_matrix[i][j] += (key_matrix[i][x] *
                                        column_matrix[x][j])

            cipher_matrix[i][j] = cipher_matrix[i][j] % 26

    CipherText = []
    for i in range(n):
        CipherText.append(chr(cipher_matrix[i][0] + 65))

    return "".join(CipherText)


def decrypt(cipher_text, key):

    key_matrix = [[8, 5, 10], [21, 8, 21], [21, 8, 12]]
    n = len(cipher_text)
    for i in range(n):
        for j in range(1):
            cipher_matrix[i][j] = 0
            for x in range(n):
                cipher_matrix[i][j] += (key_matrix[i][x] *
                                        column_matrix[x][j])

            cipher_matrix[i][j] = cipher_matrix[i][j] % 26

    text = digits_to_text(cipher_text)
    decrypted = " ".join(text)

    return decrypted


text = input("Enter Plain Text: ")
key = input("Enter key: ")

encrypted_text = encrypt(text, key)
print("Encrypted Text: ", encrypted_text)

decrypted_text = decrypt(encrypted_text, key)
print("Decrypted Text: ", decrypted_text)
