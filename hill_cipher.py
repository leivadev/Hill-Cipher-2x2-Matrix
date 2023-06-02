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
        for i in range(2):
            row = []
            for j in range(2):
                element = int(input(f"Enter element [{i}][{j}]: "))
                row.append(element)
            new_key_matrix.append(row)
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

            encrypted = hill_encrypt(word.upper(), key_matrix)
            print("Word:", word)
            print("Encrypted word:", encrypted)

        elif choice == "3":
            encrypted = input(str("Enter the encrypted word: "))
            if len(encrypted) != 4:
                print("You need to input 4 letters!\n")
                continue
            decrypted = hill_decrypt(encrypted.upper(), key_matrix)
            print("Encrypted word:", encrypted)
            print("Decrypted word:", decrypted)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
