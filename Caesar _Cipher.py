#coder:Shivam Kafle
# Importing string module which is used to define the variable "charctr" as a concatenation of the string of uppercase letters from the ASCII character set
import string
import os

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
charctr = string.ascii_uppercase + string.ascii_uppercase
#defining users which greets the user and explains the purpose of program.
"""
This is the code of the ceaser cipher game made by:
Name: Shivam Kafle 
This program implements the Caesar Cipher, which is a simple substitution cipher that shifts the letters of an input message by a fixed number of positions down the alphabet.
The program prompts the user to choose whether they want to encrypt or decrypt a message, and then prompts them for the message to be encrypted/decrypted and the shift number. It then returns the encrypted/decrypted message to the user.
The program also includes the option to read messages from a file and encrypt/decrypt them, as well as write the resulting messages to a new file.
Functions:
- welcome(): greets the user and explains the purpose of the program
- enter_message(): prompts the user to choose whether they want to encrypt or decrypt a message
- encrypt(): function to encrypt the input message
- decrypt(): function to decrypt the input message
- is_file(filename): function to check if a file exists
- process_file(filename, mode): function to read from a file and encrypt or decrypt messages
- write_messages(messages): function to write messages to a file
- message_or_file(): function to prompt the user for mode, message, or filename
- main(): main function to run the program
"""

# defining functions 
#coder:Shivam Kafle

def welcome():
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text with the Caesar Cipher.")


#defining a function to prompt the user to choose whether they want to encrypt or decrypt a message

#coder:Shivam Kafle
def enter_message():
    while True:
        user = input("Would you like to encrypt (e) or decrypt (d): ")
        if user.lower() == 'e':
            encrypt()
            break
        elif user.lower() == 'd':
            decrypt()
            break
        else:
            print("Invalid Syntax")

#function to encrypt by shifting the letters of input message 

#coder:Shivam Kafle
def encrypt():
    
    while True:
        encrypt = list(input("What message would you like to encrypt: ").upper())
        shift = input("What is the shift number: ")
        try:
            shift = int(shift.strip())
            break
        except ValueError:
            print("Invalid shift. Please enter a valid integer.")
            continue
    for i in range(len(encrypt)):
        if encrypt[i] == ' ':
            encrypt[i] == ' '
        else:
            var = charctr.index(encrypt[i]) + shift
            encrypt[i] = charctr[var]
    print(''.join(map(str, encrypt)))

#defining function to decrypt the input message
#coder:Shivam Kafle
def decrypt():
    decrypt = list(input("What message would you like to decrypt: ").upper())
    while True:
        shift = input("What is the shift number: ")
        try:
            shift = int(shift.strip())
            break
        except ValueError:
            print("Invalid shift. Please enter a valid integer.")
            continue
    for i in range(len(decrypt)):
        if decrypt[i] == ' ':
            decrypt[i] = ' '
        else:
            var = charctr.index(decrypt[i]) - shift
            decrypt[i] = charctr[var]
    print(''.join(map(str, decrypt)))


# Function to check if a file exists
#coder:Shivam Kafle
def is_file(filename):
    return os.path.isfile(filename)


# Function to read from a file and encrypt or decrypt messages
#coder:Shivam Kafle
def process_file(filename, mode):
    messages = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if mode == 'e':
                messages.append(encrypt(line))
            else:
                messages.append(decrypt(line))
    return messages


# Function to write messages to a file
#coder:Shivam Kafle
def write_messages(messages):
    with open('results.txt', 'w') as f:
        for message in messages:
            f.write(message + '\n')


# Function to prompt the user for mode, message, or filename
#coder:Shivam Kafle
def message_or_file():
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ")
        if mode in ['e', 'd']:
            break
        print("Invalid Mode")
    
    while True:
        source = input("Would you like to read from a file (f) or the console (c)? ")
        if source in ['f', 'c']:
            break
        else:
            print("Invalid Source")
    
    if source == 'f':
        while True:
            filename = input("Enter a filename: ")
            if is_file(filename):
                break
            print("Invalid Filename")
        return (mode, None, filename)
    else:
        message = input("What message would you like to {}: ".format('encrypt' if mode == 'e' else 'decrypt')).upper()
        return (mode, message, None)

# Main function
#coder:Shivam Kafle

#calling the functions defined above as welcome and enter_message
#validating the program, whether the user wants to continue or end the program
#if the user wants to end the program, it displays a thank you message
def main():
    welcome()
    while True:
        mode, message, filename = message_or_file()
        if filename:
            messages = process_file(filename, mode)
            write_messages(messages)
            print("Results written to results.txt")
        else:
            if mode == 'e':
                print("Encrypted message:", encrypt())
            else:
                print("Decrypted message:", decrypt())
        again = input("Would you like to encrypt or decrypt another message? (y/n): ")
        if again.lower() == 'n':
            print("Thank you for using Caesar Cipher.")
            break

print(__doc__)
if __name__=="__main__":
    main()  #coder:Shivam Kafle
