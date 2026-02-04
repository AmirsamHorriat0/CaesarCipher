# CaesarCipher
Simple CLI Caesar encrypt and decryption system using python 
# How Caesar cipher works
The Caesar Cipher is a substitution cipher where each letter in the text is shifted by a fixed number of positions in the alphabet.

Example (Shift = 3):

Plaintext:  HELLO
Encrypted:  KHOOR

Encrypted Letter = (Original Position + Shift) % 26
Decrypted Letter = (Original Position - Shift) % 26

The modulo (% 26) ensures the alphabet wraps around instead of going out of range.
# Installation
Clone the repository:
```
git clone https://github.com/AmirsamHorriat0/CaesarCipher.git
cd CaesarCipher
```
# Usage
```
python3 Caesar.py
```
> [!NOTE]
> No external library , raw python 

