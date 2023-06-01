# Hill Cipher Encryption and Decryption (for 2x2 matrix)

This repository contains a Python implementation of the Hill cipher encryption and decryption algorithm.

**The Hill cipher** is a polygraphic substitution cipher based on **linear algebra** that operates on blocks of 2 or 3 letters at a time (depending on the word), each letter represented by a number in modulo 26, and using a key matrix with nxn dimension (there's a 2x2 default key matrix in the code). The implementation is done purely in Python, without relying on external libraries for matrix calculations.

## Introduction

This code was developed as a college final project to gain a deeper understanding of matrix operations and cryptography. The objective was to implement the Hill cipher encryption and decryption algorithm for any 4 letter word from scratch, without using any external libraries or predefined matrix functions.

I aimed to enhance my knowledge about matrix, determinant, modular arithmetic, and encryption techniques by coding the Hill cipher algorithm manually. The project allowed us to explore the fundamental concepts underlying the Hill cipher and gain practical experience in implementing mathematical algorithms in Python.

## Usage

To use the code, you can follow these steps:

1. Clone the repository:

   `git clone https://github.com/Luislev/HillCipher_2x2.git`

2. navigate to the directory and run the 'HillCipher.py' file:

    `python3 HillCipher.py`

Once it's done, the program will present a menu with the following options:
 - **About key matrix**: Edit, view, or reset the current key matrix.
 - **Encrypt word**: Enter a word and encrypt it using the Hill cipher.
 - **Decrypt word**: Enter an encrypted word and decrypt it using the Hill cipher.
 - **Exit**: Quit the program.

Follow instructions to interact with the program.

You need to have Python 3.x installed on your system to run the program.

## Contributing

Contributions to this project are welcome. If you find any issues or want to enhance the program, feel free to create a pull request!🤗

## Author

Luis Leiva - Software Development Student at _Universidad Tecnológica de Panamá_

## References
 - [Hill cipher - Wikipedia](https://www.wikipedia.org/wiki/Hill_cipher)
 - [Hill Cipher - GeeksforGeeks](https://www.geeksforgeeks.org/hill-cipher/)
