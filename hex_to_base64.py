#this program converts hex to base64
from base64 import b64encode

def hex_to_byte(s):
    arr = bytes.fromhex(s)
    return arr

if __name__ == '__main__':
    test = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    byte_arr = hex_to_byte(test)
    print(b64encode(byte_arr), end=' ')