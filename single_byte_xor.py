
encoded = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
import binascii
nums = binascii.unhexlify(encoded)
result = []
#for key in range(256):
#    for num in nums:
#        result.append(chr(num ^ key))
#print(''.join(result))

strings = (''.join(chr(num ^ key) for num in nums) for key in range(256))
print(max(strings, key=lambda s: s.count( ' ')))

#print(nums)

