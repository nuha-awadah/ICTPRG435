#!/usr/bin/env python
"""
SYNOPSIS

    TODO This describes how to run the script via CLI.
    e.g. helloworld [-h,--help] [-v,--verbose] [--version]

DESCRIPTION

    TODO This describes how to use this script.

EXAMPLES

    TODO: Show some examples of how to use this script.

AUTHOR

    30148167@tafe.wa.edu.au

LICENSE

    This script is the exclusive and proprietary property of
    TiO2 Minerals Consultants Pty Ltd. It is only for use and
    distribution within the stated organisation and its
    undertakings.

VERSION

    $Id$

Scenario 2: Caesar Cipher Encryption Script
Create a script file that follows the provided pseudocode in Scenario 2.
File Name: caesar_new.py
Requirements:
Include completed headers at the top of the script using the TMC_Header template.
Add comments above each major block of code to explain its purpose.
Double-check for any missing steps in your pseudocode and update the code as necessary.

"""
# used to check if the file exists
import os
# using pycryptodome to hash the password as password verification
# SHA-256 produces a fixed-length 256-bit hash password
from Crypto.Hash import SHA256

# a function to shift one uppercase letter.
def shift_char_uppercase(character, shift_value):
    # convert the uppercase letter into its ASCII number
    ascii_value = ord(character)
    # convert to a position from 0 to 25, add the shift, wrap around using modulo 26, and convert back to ASCII
    new_ascii_value = ((ascii_value - ord('A') + shift_value) % 26) + ord('A')
    # convert the new ASCII number back into a character
    return chr(new_ascii_value)


# a function to shift one lowercase letter.
def shift_char_lowercase(character, shift_value):
    # convert the lowercase letter into its ASCII number
    ascii_value = ord(character)
    # chift the letter within the lowercase alphabet, wrapping around after z
    new_ascii_value = ((ascii_value - ord('a') + shift_value) % 26) + ord('a')
    # convert the new ASCII number back into a character
    return chr(new_ascii_value)


# s function to shift all letters in the content.
def shift_letters(content, shift_value):
    # initialized a variable to put the results in
    result = ""
    # looping through every character in the content.
    for character in content:
        # Check whether the character is an uppercase English letter.
        if 'A' <= character <= 'Z':
            # Call the uppercase shifting function.
            shifted_char = shift_char_uppercase(character, shift_value)
        # Otherwise, check whether the character is a lowercase English letter.
        elif 'a' <= character <= 'z':
            # Call the lowercase shifting function.
            shifted_char = shift_char_lowercase(character, shift_value)
        # Handle characters that are not English letters.
        else:
            # Keep numbers, punctuation, spaces and other characters unchanged.
            shifted_char = character
        # Append the processed character to the result string.
        result += shifted_char
    # Return the complete shifted content after the loop finishes.
    return result


# Define the Caesar cipher encryption function.
def encrypt_caesar_cipher(content, shift_value):
    # Shift letters forward using the supplied shift value.
    return shift_letters(content, shift_value)


# Define the Caesar cipher decryption function.
def decrypt_caesar_cipher(content, shift_value):
    # Reverse the shift to recover the original letters.
    return shift_letters(content, -shift_value)


# Define a function to encrypt a text file using an integer password.
def encrypt_file(file_path, password):
    # Open the original file for reading as UTF-8, preserving line endings; close it automatically afterwards.
    with open(file_path, 'r', encoding='utf-8', newline='') as file:
        # Read the entire file into a string.
        file_content = file.read()

    # Encrypt the file content using the password as the shift value.
    encrypted_content = encrypt_caesar_cipher(file_content, password)
    # Convert the password to text, then bytes, and generate its SHA256 hash as hexadecimal text.
    password_hash = SHA256.new(str(password).encode('utf-8')).hexdigest()
    # Append the required .encrypted extension to the original file path.
    encrypted_file_path = file_path + '.encrypted'

    # Open the encrypted output file for writing; an existing output file will be overwritten.
    with open(encrypted_file_path, 'w', encoding='utf-8', newline='') as file:
        # Write the password hash on the first line, followed by a newline.
        file.write(password_hash + '\n')
        # Write the encrypted content after the hash.
        file.write(encrypted_content)

    # Display the success message and encrypted file path.
    print('File encrypted successfully. Saved as ' + encrypted_file_path)


# Define a function to decrypt an encrypted text file.
def decrypt_file(encrypted_file_path, password):
    # Open the encrypted file for reading as UTF-8, preserving line endings.
    with open(encrypted_file_path, 'r', encoding='utf-8', newline='') as file:
        # Read the first line containing the stored password hash and remove its trailing newline.
        stored_hash = file.readline().rstrip('\n')
        # Read the remaining encrypted content.
        encrypted_content = file.read()

    # Check that the stored hash has 64 characters and contains only lowercase hexadecimal digits.
    if len(stored_hash) != 64 or any(c not in '0123456789abcdef' for c in stored_hash):
        # Display an error if the stored hash has an invalid format.
        print('Invalid encrypted file format.')
        # Stop this function without decrypting the file.
        return

    # Generate a SHA256 hash from the password entered by the user.
    password_hash = SHA256.new(str(password).encode('utf-8')).hexdigest()
    # Compare the entered password hash with the stored password hash.
    if password_hash != stored_hash:
        # Display an error when the hashes do not match.
        print('Incorrect password.')
        # Stop this function without creating a decrypted file.
        return

    # Decrypt the content by reversing the Caesar cipher shift.
    decrypted_content = decrypt_caesar_cipher(encrypted_content, password)
    # Remove the .encrypted suffix to restore the original file path.
    decrypted_file_path = encrypted_file_path[:-len('.encrypted')]

    # Check whether the original output path already exists.
    if os.path.exists(decrypted_file_path):
        # Warn the user to move or rename the existing file to avoid overwriting it.
        print('Output file already exists. Rename or move it first.')
        # Stop this function without writing the decrypted content.
        return

    # Create a new UTF-8 file in exclusive creation mode (x), which refuses to overwrite existing files.
    with open(decrypted_file_path, 'x', encoding='utf-8', newline='') as file:
        # Write the decrypted content to the new file.
        file.write(decrypted_content)

    # Display the success message and decrypted file path.
    print('File decrypted successfully. Saved as ' + decrypted_file_path)


# Define the main function that controls user input and program execution.
def main():

    # Ask for an operation, remove surrounding whitespace and convert it to lowercase.
    operation_choice = input('Select operation either Encrypt or Decrypt: ').strip().lower()
    # Check whether the operation is neither encrypt nor decrypt.
    if operation_choice not in ('encrypt', 'decrypt'):
        # Display an error message for an invalid operation.
        print('Invalid operation choice.')
        # Exit the main function.
        return

    # Ask for the file path and remove surrounding whitespace.
    file_path = input('Enter the file path: ').strip()
    # Check whether the path does not point to an existing regular file.
    if not os.path.isfile(file_path):
        # Display an error message for a missing or invalid file path.
        print('File not found. Please check the file path.')
        # Exit the main function.
        return

    # For decryption, check whether the file lacks the required .encrypted suffix.
    if operation_choice == 'decrypt' and not file_path.endswith('.encrypted'):
        # Display an error message for an invalid encrypted file extension.
        print('Invalid encrypted file extension.')
        # Exit the main function.
        return

    # Start a try block to handle invalid password input.
    try:
        # Ask for the password and convert the input string into an integer.
        password = int(input('Enter an integer password: '))
    # Catch a ValueError if the input cannot be converted to an integer.
    except ValueError:
        # Tell the user that the password must be an integer.
        print('Invalid password. Enter an integer.')
        # Exit the main function.
        return

    # Start a try block to handle errors during file processing.
    try:
        # Check whether the user selected encryption.
        if operation_choice == 'encrypt':
            # Call the file encryption function with the file path and password.
            encrypt_file(file_path, password)
        # Otherwise, the validated operation must be decryption.
        else:
            # Call the file decryption function with the file path and password.
            decrypt_file(file_path, password)
    # Catch file system errors, text encoding errors or invalid values during processing.
    except (OSError, UnicodeError, ValueError):
        # Display an error message instead of allowing the program to crash.
        print('Unable to read or write the file.')

    print(f"\nID: 30148167, Initials:  NABMY")

# Check whether this Python file is being run directly rather than imported.
if __name__ == '__main__':
    # Call the main function to start the program.
    main()