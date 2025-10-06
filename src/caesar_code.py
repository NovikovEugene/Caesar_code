#!/usr/bin/env python3

import sys

def caesar_code(text, shift, mode):

    if not text.isascii():
        raise ValueError("The script does not support your language yet")
    
    if mode == 'encode':
        shift_direct = shift
    else:
        shift_direct = -shift
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                start = ord('a')
            else:
                start = ord('A')
            result += chr((ord(char) - start + shift_direct) % 26 + start)
        else:
            result += char
    return result

def caesar():
    if len(sys.argv) != 4:
        raise ValueError("Usage: python3 caesar.py <encode|decode> <text> <shift>")
    
    mode = sys.argv[1]
    text = sys.argv[2]
    shift = int(sys.argv[3])
    
    if mode not in ['encode', 'decode']:
        raise ValueError("Invalid mode. Use 'encode' or 'decode'.")
    
    result = caesar_code(text, shift, mode)
    print(result)
    
if __name__ == "__main__":
    try:
        caesar()
    except Exception as e:
        print(e)