def load_key():
    with open("key.txt", "r") as f:
        return f.read().strip()

def xor_encrypt(plaintext, key):
    result = []
    for i in range(len(plaintext)):
        result.append(chr(ord(plaintext[i]) ^ ord(key[i % len(key)])))
    return "".join(result)

def encrypt_to_hex(text, key):
    encrypted = xor_encrypt(text, key)
    return encrypted.encode().hex()

def decrypt_from_hex(hex_text, key):
    encrypted = bytes.fromhex(hex_text).decode()
    return xor_encrypt(encrypted, key)
