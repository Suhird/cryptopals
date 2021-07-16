## This program converts hex to base64
## input: hex string
## output: base64 encoded string
## usage:-
## >>> python hex_to_base64.py [HEX STRING]
##

from base64 import b64encode
import sys

from utils.cryptopals import hex_to_byte


if __name__ == '__main__':
    #test = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    input_str = sys.argv[1]
    byte_arr = hex_to_byte(input_str)
    print(b64encode(byte_arr), end=' ')