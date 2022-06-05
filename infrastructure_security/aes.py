from Cryptodome.Cipher import AES
key = b'0123456789abcdef'
IV=b'0123456789abcdef'
mode = AES.MODE_CFB
encryptor = AES.new(key, mode,IV=IV)
text = b'hello'
ciphertext = encryptor.encrypt(text).hex()
print(ciphertext)