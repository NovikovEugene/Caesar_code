# Caesar Cipher: My First Python Project

A Caesar cipher is a type of substitution cipher in which each character in the plaintext is replaced by a character located a constant number of positions to the left or right of it in the alphabet. The cipher was named after the Roman general Gaius Julius Caesar, who used it for secret correspondence with his generals. Like all monoalphabetic ciphers, the Caesar cipher is easily broken and has almost no practical use. However, it is considered one of the simplest and most widely known encryption methods.

## Usage

$ python3 caesar_code.py <encode|decode> <text> <shift>

* encode|decode - encode/decode text using shift
* text - text to encrypt
* shift - encryption step, how many characters to shift

## Limitations

* The script checks the number of arguments
* The script does not work with Cyrillic characters
* The range of characters to encrypt is a-z and A-Z (Numbers are ignored)
* If the text contains more than one word, use quotation marks, ' ' or " "