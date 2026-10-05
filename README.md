AES-128 Encryption & Decryption
A  Python implementation of AES-128, supporting ECB and CBC modes, PKCS#7 padding, command-line encryption/decryption, and text-file encryption/decryption along with the implementation of vigenere cipher.
This project was implemented without using Python's built-in cryptography libraries for the AES algorithm. The AES transformations and key expansion were implemented manually to understand how AES works internally.

Features
•	AES-128 encryption
•	AES-128 decryption
•	ECB mode
•	CBC mode
•	PKCS#7 padding and unpadding
•	Vigenère cipher
•	Command-line interface
•	Text encryption/decryption
•	File encryption/decryption

AES-128
AES operates on blocks of 128 bits (16 bytes).
AES-128 uses a 128-bit (16-byte) key and performs:
•	1 initial AddRoundKey operation
•	9 standard rounds
•	1 final round without MixColumns
The standard encryption round consists of:
SubBytes
ShiftRows  
MixColumns
AddRoundKey
The final round omits MixColumns.

ECB Mode
ECB (Electronic Codebook) encrypts every block independently.
Plaintext Block 1 → AES → Ciphertext Block 1
Plaintext Block 2 → AES → Ciphertext Block 2
Plaintext Block 3 → AES → Ciphertext Block 3
PKCS#7 padding is applied before encryption.

CBC Mode
CBC (Cipher Block Chaining) links consecutive blocks together.
For encryption:
P1 XOR IV → AES → C1
P2 XOR C1 → AES → C2
P3 XOR C2 → AES → C3
For decryption:
C1 → AES⁻¹ → XOR IV → P1
C2 → AES⁻¹ → XOR C1 → P2
C3 → AES⁻¹ → XOR C2 → P3
The implementation generates a random 16-byte IV during CBC encryption.
The IV is not secret and must be supplied during decryption.

PKCS#7 Padding
AES requires input blocks of exactly 16 bytes.
PKCS#7 padding is therefore used when the plaintext is not a multiple of 16 bytes.
For example:
Hello
is 5 bytes.
It receives 11 bytes of padding:
48 65 6c 6c 6f 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b
If the plaintext is already exactly 16 bytes, an entire additional block of:
10 10 10 10 10 10 10 10
10 10 10 10 10 10 10 10
is added.

Command-Line Usage:

Vigenère

Encrypt:
python main.py -e -key KEY vigenere "Hello World"

Decrypt:
python main.py -d -key KEY vigenere "EncryptedText"

AES-128 ECB

Encrypt text:
python main.py -e -key 000102030405060708090a0b0c0d0e0f AES ECB "Hello"
The output is the ciphertext in hexadecimal(94e11c4e7b21b9e66c0082a5089604ea)

Decrypt text:
python main.py -d -key 000102030405060708090a0b0c0d0e0f AES ECB "CIPHERTEXT"

AES-128 CBC

Encrypt text:
CBC encryption automatically generates a random IV.
python main.py -e -key 000102030405060708090a0b0c0d0e0f AES CBC "Hello"
Example output:
Initialisation Vector: db9058680db4a65015fdfd7c0e3246d3
Ciphertext: bff59076749fd903accb2cfed6058721
The IV will be different each time because it is randomly generated.

Decrypt text:
Use the IV generated during encryption:
python main.py -d -key 000102030405060708090a0b0c0d0e0f -iv db9058680db4a65015fdfd7c0e3246d3 AES CBC "bff59076749fd903accb2cfed6058721"
The result will be:
Hello

File Encryption
The -f option enables file encryption/decryption.

ECB file encryption:
python main.py -e -key 000102030405060708090a0b0c0d0e0f AES ECB -f input.txt encrypted.txt

ECB file decryption:
python main.py -d -key 000102030405060708090a0b0c0d0e0f AES ECB -f encrypted.txt decrypted.txt

CBC file encryption:
python main.py -e -key 000102030405060708090a0b0c0d0e0f AES CBC -f input.txt encrypted.txt
The program generates and displays the IV.
Example:
Initialisation Vector: <IV>
Save this IV for decryption.

CBC file decryption:
python main.py -d -key 000102030405060708090a0b0c0d0e0f AES CBC -f encrypted.txt decrypted.txt -iv <IV>
After decryption, decrypted.txt should contain the original plaintext.


