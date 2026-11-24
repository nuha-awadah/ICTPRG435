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

import os

# Move letters forward or backward in the alphabet.
def shift_letters(text, password):

    # initialize the variable result to keep the result in
    result = ""

    # looping for each letters in the text
    for letter in text:
        # if the letters are uppercase,
        if "A" <= letter <= "Z":
            number = (ord(letter) - ord("A") + password) % 26
            result += chr(ord("A") + number)
        # if the letters are lowercase then
        elif "a" <= letter <= "z":
            number = (ord(letter) - ord("a") + password) % 26
            result += chr(ord("a") + number)

        # if the character are non-alphabetical, add the non-alphabetical
        # directly in the result without changes
        else:
            result += letter

    return result


# read a normal text file, encrypt it, and save a new file.
def encrypt_file(filePath, password):

    # going to the file path and opening the file
    with open(filePath, "r", encoding="utf-8") as file:
        # putting the text from the file to the text variable
        text = file.read()

    # CHECK: helps us notice many wrong passwords during decryption.
    result = shift_letters("CHECK:" + text, password)
    # make new encrypted file and safe in same folder
    newFile = filePath + ".encrypted"

    # write the new file with the result in it
    with open(newFile, "w", encoding="utf-8") as file:
        file.write(result)

    # print the new file name to the user
    print("File encrypted: " + newFile)


# read an encrypted file and restore the original text file.
def decrypt_file(filePath, password):
    if not filePath.endswith(".encrypted"):
        print("Error: Choose a file ending with .encrypted")
        return

    with open(filePath, "r", encoding="utf-8") as file:
        text = file.read()

    result = shift_letters(text, -password)
    if not result.startswith("CHECK:"):
        print("Error: Wrong password or invalid encrypted file.")
        return

    # Remove CHECK: and remove .encrypted from the filename.
    result = result[6:]
    newFile = filePath[:-len(".encrypted")]

    with open(newFile, "w", encoding="utf-8") as file:
        file.write(result)

    print("File decrypted: " + newFile)


# Ask what the user wants and call the correct function.
def main():
    operation = input("Encrypt or Decrypt? ").strip().lower()

    # check if the input is valid
    if operation != "encrypt" and operation != "decrypt":
        # prints an error message to the user
        print("Error: Choose Encrypt or Decrypt.")
        return

    # request the file path from the user
    filePath = input("Enter file name or path: ").strip()
    # checks if the file path is valid
    if not os.path.isfile(filePath):
        # prints an error message to the user
        print("Error: File not found.")
        return

    #try except block
    try:
        # request the password from the user
        password = int(input("Enter a number for the password: "))
    except ValueError:
        # prints an error message to the user if the password is not a whole number
        print("Error: Password must be a whole number.")
        return

    try:
        # check if the operation inputted by the user is encrypt
        if operation == "encrypt":
            # call the encryption function
            encrypt_file(filePath, password)
        else:
            # call the decryption function
            decrypt_file(filePath, password)

    # handle system errors or character encoding errors if
    except (OSError, UnicodeError):

        #display an error message if the file cannot be read or saved
        print("Error: Could not read or save the file.")


# check if the script is being executed directly
if __name__ == "__main__":

    #calls the main function to start the program
    main()

