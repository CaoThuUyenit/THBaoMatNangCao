from cipher.caesar import ALPHABET
class CaesarCipher:

    def __init__(self):
        self.alphabet = ALPHABET

    def encrypt_text(self, plain_text, key):
        result = ""
        alphabet_len = len(self.alphabet)

        for char in plain_text:
            if char.upper() in self.alphabet:
                index = self.alphabet.index(char.upper())
                new_index = (index + key) % alphabet_len
                result += self.alphabet[new_index]
            else:
                result += char

        return result

    def decrypt_text(self, cipher_text, key):
        return self.encrypt_text(cipher_text, -key)