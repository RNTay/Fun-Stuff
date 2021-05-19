def caesar_shift_encrypt(file_name: str, shift: int):
    """Encryption shifts characters to the right.
    e.g. A (shift 3) -> D"""
    letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    with open(file_name, 'r') as file:
        plaintext = file.readlines()
    with open(file_name, 'w') as file:
        for plaintext_line in plaintext:
            ciphertext_line = ''
            for character in plaintext_line:
                character = character.upper()
                if character in letters:
                    ciphertext_line += letters[(letters.index(character) + shift) % len(letters)]
                else:
                    ciphertext_line += character
            file.write(ciphertext_line)


def caesar_shift_decrypt(file_name: str, shift: int):
    """Decryption shifts characters to the left.
    e.g. E (shift 3) -> B"""
    letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    with open(file_name, 'r') as file:
        ciphertext = file.readlines()
    with open(file_name, 'w') as file:
        for ciphertext_line in ciphertext:
            plaintext_line = ''
            for character in ciphertext_line:
                character = character.upper()
                if character in letters:
                    plaintext_line += letters[(letters.index(character) - shift) % len(letters)]
                else:
                    plaintext_line += character
            file.write(plaintext_line)
