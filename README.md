# Encryption and Decryption Technique

![Encryption](https://img.shields.io/badge/Encryption-Algorithm-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-brightgreen)
![License](https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png)

This project provides a custom encryption and decryption technique based on an alphanumeric constant. It uses a unique method to obfuscate text, making it unreadable without the correct decryption key.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Encryption](#encryption)
  - [Decryption](#decryption)
- [License](#license)

## Description

The technique leverages a user-provided alphanumeric constant to determine the transformation applied to each character in the plaintext. This makes the encrypted message highly secure and hard to decipher without the correct constant.

## Features

- **Customizable Constants:** Use any combination of alphanumeric characters as the constant.
- **Secure Encryption:** Random characters inserted based on the constant to obfuscate the message.
- **Easy Decryption:** Decrypt messages using the same constant.

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/xtasy94/encryption-decryption-technique.git
   ```
2. **Navigate to the project directory:**
   ```sh
   cd encryption-decryption-technique
   ```

## Usage

### Encryption

Run the `encryption.py` script to encrypt a plaintext message:
```sh
python encryption.py
```
You will be prompted to enter an alphanumeric constant and a plaintext message. The script will output the encrypted message.

### Decryption

Run the `decryption.py` script to decrypt an encrypted message:
```sh
python decryption.py
```
You will be prompted to enter the same alphanumeric constant and the encrypted message. The script will output the decrypted message.

## Example

### Encryption

1. **Input:**
   ```
   Constant: 324pu2hp
   Plaintext: Hello World
   ```
2. **Output:**
   ```
   Encrypted Message: fjsHy6eqEeult6H8ECmKI4slt7FXgGo   o1uWMpt03bylHQZQGarWp0NWJY4Ldx3oqWTr7wlVj7Fd
   ```

### Decryption

1. **Input:**
   ```
   Constant: 324pu2hp
   Encrypted Message: fjsHy6eqEeult6H8ECmKI4slt7FXgGo   o1uWMpt03bylHQZQGarWp0NWJY4Ldx3oqWTr7wlVj7Fd
   ```
2. **Output:**
   ```
   Decrypted Message: Hello World
   ```

## License

Shield: [![CC BY-NC-ND 4.0][cc-by-nc-nd-shield]][cc-by-nc-nd]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-NoDerivs 4.0 International License][cc-by-nc-nd].

[![CC BY-NC-ND 4.0][cc-by-nc-nd-image]][cc-by-nc-nd]

[cc-by-nc-nd]: http://creativecommons.org/licenses/by-nc-nd/4.0/
[cc-by-nc-nd-image]: https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png
[cc-by-nc-nd-shield]: https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg
