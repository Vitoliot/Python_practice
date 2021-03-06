import string
alphapet_low = list(string.ascii_lowercase)
alphapet_up = list(string.ascii_uppercase)

def encrypt_caesar(plaintext, shift = 3):
    ciphertext = ""
    for sym in plaintext:
      if sym in alphapet_low:
        ciphertext += alphapet_low[(alphapet_low.index(sym) + shift)%26]
      elif sym in alphapet_up:
        ciphertext += alphapet_up[(alphapet_up.index(sym) + shift)%26]
      else: ciphertext += sym
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3):
    plaintext = ""
    for sym in ciphertext:
      if sym in alphapet_low:
        plaintext += alphapet_low[(alphapet_low.index(sym) - shift)%26]
      elif sym in alphapet_up:
        plaintext += alphapet_up[(alphapet_up.index(sym) - shift)%26]
      else: plaintext += sym
    return plaintext


text = input()
shift = int(input())
print(encrypt_caesar(text, shift))
print(decrypt_caesar(encrypt_caesar(text, shift), shift))