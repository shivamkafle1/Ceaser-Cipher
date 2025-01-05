
# Caesar Cipher Game by Shivam Kafle!



Welcome to the **Caesar Cipher Game**, a Python program that demonstrates the Caesar Cipher encryption and decryption technique. This project is a fun way to explore the concept of substitution ciphers, often regarded as one of the simplest encryption methods.
![image](https://github.com/user-attachments/assets/7204b215-384a-48cc-b064-02a279a2bdf1)


---

## Program Overview

The **Caesar Cipher Game** shifts the letters of an input message by a fixed number of positions in the alphabet. This program offers two primary functionalities:
1. **Encryption:** Converts a plaintext message into an encoded message by shifting the letters forward.
2. **Decryption:** Reverts the encoded message back to plaintext by shifting the letters backward.

Additionally, the program supports:
- Reading messages from files for encryption or decryption.
- Writing the results to a new file.


---

## Features

- **User-Friendly Interface:** Easily encrypt or decrypt messages by following the on-screen prompts.
- **Flexible Input Options:** Choose between inputting messages directly or reading from a file.
- **Error Handling:** Provides validations to ensure inputs like shift numbers and filenames are correct.

---

## Code Explanation

### 1. **Core Functions**

- **`welcome()`**  
  Greets the user and explains the purpose of the program.

- **`enter_message()`**  
  Prompts the user to choose whether to encrypt or decrypt a message and directs them accordingly.

- **`encrypt()`**  
  Encrypts a given message by shifting each character forward by a specified number of positions.

- **`decrypt()`**  
  Decrypts an encoded message by shifting each character backward by the specified number of positions.

- **`is_file(filename)`**  
  Checks if the specified file exists.

- **`process_file(filename, mode)`**  
  Reads messages from a file and processes them (encrypts or decrypts) based on the chosen mode.

- **`write_messages(messages)`**  
  Saves the processed messages into a new file called `results.txt`.

- **`message_or_file()`**  
  Guides the user in selecting input options: whether to work with a file or input messages directly.

---

### 2. **Main Functionality**

- **`main()`**  
  Orchestrates the program flow:
  - Greets the user.
  - Accepts user inputs for encryption or decryption.
  - Handles file processing or direct message input.
  - Outputs results or saves them to a file.
  - Repeats the process until the user opts to quit.

---

## Installation and Usage

1. Clone this repository or download the code as a ZIP file.
2. Ensure you have Python installed (preferably version 3.6 or later).
3. Run the program in your terminal using the command:
   ```bash
   python caesar_cipher.py
   ```

---

## Image Template Placeholder

Below are placeholders where you can add images or screenshots demonstrating your project in action:

### 1. Program Interface
*Insert an image showing the program running in the terminal with sample inputs.*

### 2. File Encryption/Decryption
*Insert an image showing how the program processes messages from a file.*

---

## Example Usage

### Encrypting a Message:
```
Would you like to encrypt (e) or decrypt (d): e
What message would you like to encrypt: HELLO WORLD
What is the shift number: 3
Encrypted message: KHOOR ZRUOG
```

### Decrypting a Message:
```
Would you like to encrypt (e) or decrypt (d): d
What message would you like to decrypt: KHOOR ZRUOG
What is the shift number: 3
Decrypted message: HELLO WORLD
```

---

## File Processing Example

- **Input File Content:**  
  `input.txt`:
  ```
  SECRET MESSAGE
  ANOTHER MESSAGE
  ```

- **Output File Content:**  
  `results.txt` (after encryption with a shift of 5):
  ```
  XJHWJY RJXXFLJ
  FSTYMJW RJXXFLJ
  ```

---

## Contributing

Feel free to fork this repository, enhance the features, or report issues. Contributions are always welcome!

---

## Author

- **Shivam Kafle**  
  Connect with me on GitHub to explore more exciting projects.

---

## License

This project is licensed under Shivam Kafle.
