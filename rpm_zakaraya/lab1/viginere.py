import string
alphapet_low = list(string.ascii_lowercase)
alphapet_up = list(string.ascii_uppercase)

def encrypt_vigenere(plaintext, key):
    ciphertext = ""
    if len(plaintext) > len(key):
        i = len(plaintext) - len(key)
        for n_sym in range(i):
            key += key[n_sym]
    for sym in range(len(plaintext)):
      if plaintext[sym] in alphapet_low:
        ciphertext += alphapet_low[((alphapet_low.index(plaintext[sym]) + (ord(key[sym]) - 97)))%26]
      elif plaintext[sym] in alphapet_up:
        ciphertext += alphapet_up[((alphapet_up.index(plaintext[sym]) + (ord(key[sym]) - 65)))%26]
      else: 
        ciphertext += plaintext[sym]
    return ciphertext


def decrypt_vigenere(ciphertext, key) -> str:
    plaintext = ""
    if len(ciphertext) > len(key):
        i = len(ciphertext) - len(key)
        for n_sym in range(i):
            key += key[n_sym]
    for sym in range(len(ciphertext)):
      if ciphertext[sym] in alphapet_low:
        plaintext += alphapet_low[((alphapet_low.index(ciphertext[sym]) - (ord(key[sym]) - 97)))%26]
      elif ciphertext[sym] in alphapet_up:
        plaintext += alphapet_up[((alphapet_up.index(ciphertext[sym]) - (ord(key[sym]) - 65)))%26]
      else: 
        plaintext += ciphertext[sym]
    return plaintext


text = input()
key = input()
print(encrypt_vigenere(text, key))
print(decrypt_vigenere(encrypt_vigenere(text, key), key))
