##A function that takes two equal-length buffers and produces their XOR combination.
##
##
##

def hex_to_byte(s):
    arr = bytes.fromhex(s)
    return arr

if __name__ == '__main__':
    str1 = '1c0111001f010100061a024b53535009181c'
    str2 = '686974207468652062756c6c277320657965'
    bytes_arr1 = hex_to_byte(str1)
    bytes_arr2 = hex_to_byte(str2)
    print([a^b for a,b in zip(str1, str2)])