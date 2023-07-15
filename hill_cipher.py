"""
This code implements a Hill cipher encryption and decryption algorithm.

The Hill cipher is a polygraphic substitution cipher that encrypts and decrypts messages using a key matrix.
The key matrix is a 2x2 matrix of integers, and the cipher operates on blocks of 2 letters at a time.

The code consists of several functions:
- letter_to_number: Converts a letter to its corresponding numerical representation.
- number_to_letter: Converts a number to its corresponding letter representation.
- determinant_matrix: Calculates the determinant of a 2x2 matrix.
- input_matrix: Prompts the user to input a new key matrix and returns it.
- inverse_matrix: Calculates the modular inverse of the key matrix.
- vector_matrix_multiplication: Performs matrix multiplication between the key matrix and a vector.
- hill_encrypt: Encrypts a word using the Hill cipher algorithm and the provided key matrix.
- hill_decrypt: Decrypts an encrypted word using the Hill cipher algorithm and the provided key matrix.
- main: It presents a menu to the user for key matrix management, word encryption, and decryption.

Note: This code uses a modulo 26 arithmetic for encryption and decryption.

Author: Luis Leiva
Date: 06/03/2023
"""

def letter_to_number(letter):
    return ord(letter) - ord('A')


def number_to_letter(number):
    return chr(number + ord('A'))


def determinant_matrix(key_matrix):
     determinant = key_matrix[0][0] * key_matrix[1][1] - key_matrix[0][1] * key_matrix[1][0]
     return determinant


def input_matrix():
    new_key_matrix = []
    print("Enter the elements of the key matrix (2x2 matrix):")
    try:
        for j in range(2):
            row = []
            for i in range(2):
                element = int(input(f"Enter element [{i}][{j}]: "))
                if element == 0 or element > 26:
                    print("You can't use this value! make sure to use a number between 1 and 26.\n")
                    return None
                row.append(element)
            new_key_matrix.append(row)
        if determinant_matrix(new_key_matrix) == 0:
            print("You can't use this key matrix! make sure that it has a non-zero determinant.\n")
            return None
        elif determinant_matrix(new_key_matrix) % 2 == 0 or determinant_matrix(new_key_matrix) % 13 == 0:
            print("You can't use this key matrix! make sure that it's not divisible by 2 or 13.\n")
            return None
        return new_key_matrix
    except ValueError:
        print("Invalid input. Please enter integers only.\n")
        return None


def inverse_matrix(key_matrix):
    determinant = determinant_matrix(key_matrix)
    scalar = 0
    if determinant == 0 or not len(key_matrix) == 2:
        return None
    for i in range(26):
        ecuation = (i * determinant) % 26
        if ecuation == 1:
            scalar = i
            break
        else:
            None
    return [[(key_matrix[1][1] * scalar) % 26, ((-1 * key_matrix[0][1] % 26) * scalar) % 26],
            [((-1 * key_matrix[1][0] % 26) * scalar) % 26, (key_matrix[0][0] * scalar) % 26]]


def vector_matrix_multiplication(key_matrix, vector):
    result = [0, 0]
    for i in range(2):
        for j in range(2):
            result[i] += key_matrix[i][j] * vector[j]
            result[i] %= 26
    return result


def hill_encrypt(word, key_matrix):
    encrypted_word = ""
    for i in range(0, len(word), 2):
        vector = [letter_to_number(word[i]), letter_to_number(word[i + 1])]
        encrypted_vector = vector_matrix_multiplication(key_matrix, vector)
        encrypted_letters = [number_to_letter(num) for num in encrypted_vector]
        encrypted_word += "".join(encrypted_letters)

    return encrypted_word


def hill_decrypt(encrypted_word, key_matrix):
    decrypted_word = ""
    for i in range(0, len(encrypted_word), 2):
        vector = [letter_to_number(encrypted_word[i]), letter_to_number(encrypted_word[i + 1])]
        decrypted_vector = vector_matrix_multiplication(inverse_matrix(key_matrix), vector)
        decrypted_letters = [number_to_letter(num) for num in decrypted_vector]
        decrypted_word += "".join(decrypted_letters)

    return decrypted_word


def main():
    key_matrix = [[3, 3], [2, 5]]
    while True:
        print("Menu:")
        print("1. About key matrix")
        print("2. Encrypt word")
        print("3. Decrypt word")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nAbout key matrix:")
            print("1. Edit the key matrix")
            print("2. See value of the key matrix")
            print("3. Reset key matrix to default value ([3, 3], [2, 5])")

            key_matrix_choice = input("Enter your choice: ")

            if key_matrix_choice == "1":
                new_key_matrix = input_matrix()
                if new_key_matrix is not None:
                    key_matrix = new_key_matrix
                    print("Key matrix updated successfully!\n")

            elif key_matrix_choice == "2":
                print("Value of Key Matrix:", key_matrix)

            elif key_matrix_choice == "3":
                if key_matrix == [[3, 3,], [2, 5]]:
                    print("You are using the default value!\n")
                else:
                    key_matrix = [[3, 3,], [2, 5]]
                    print("key matrix reset successfully!\n")

        elif choice == "2":
            word = input(str("Enter a word of 4 letters: "))
            if len(word) != 4:
                print("You need to input 4 letters!\n")
                continue
            if not word.isalpha():
                print("The input must contain letters of the alphabet only.\n")
                continue

            encrypted = hill_encrypt(word.upper(), key_matrix)
            print("Word:", word)
            print("Encrypted word:", encrypted)

        elif choice == "3":
            encrypted = input(str("Enter the encrypted word: "))
            if len(encrypted) != 4:
                print("You need to input 4 letters!\n")
                continue
            if not encrypted.isalpha():
                print("The input must contain letters of the alphabet only.\n")
                continue
            decrypted = hill_decrypt(encrypted.upper(), key_matrix)
            print("Encrypted word:", encrypted)
            print("Decrypted word:", decrypted)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a valid option.\n")


if __name__ == "__main__":
    main()
