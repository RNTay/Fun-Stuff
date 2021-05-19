#!/usr/bin/env python3

def vigenere_cipher(plaintext: str, key: str) -> str:
    """
    Encrypts the plaintext using the Vigenère cipher
    and returns the ciphertext.
    e.g. plaintext: SPLENDID
         key: LEMON
         ciphertext: DTXSAOMP
    """
    letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    key_indices = [letters.index(_) for _ in key]

    i = 0
    current_key = key_indices[i]

    ciphertext = ''

    for character in plaintext:
        cipher_character = letters[(letters.index(character) + current_key) % len(letters)]
        ciphertext += cipher_character
        i = (i+1) % len(key)
        current_key = key_indices[i]

    return ciphertext
