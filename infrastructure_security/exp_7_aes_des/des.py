from Cryptodome.Cipher import DES3
from Cryptodome import Random
key = b'Sixteen byte key'
iv = Random.new().read(DES3.block_size)
cipher = DES3.new(key, DES3.MODE_CFB, iv)
plaintext = b'HridayModi'
msg =cipher.encrypt(plaintext).hex()
print(msg)