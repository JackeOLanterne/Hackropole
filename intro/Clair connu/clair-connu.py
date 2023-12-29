import os

def keep_only_n_bytes(byte_array, n):
    # Slice the byte array to keep only the first n bytes
    result_byte_array = byte_array[:n]
    return result_byte_array

def xor_byte_arrays(array1, array2):
    # Make sure the arrays have the same length
    if len(array1) != len(array2):
        raise ValueError("Byte arrays must have the same length")

    # Perform XOR operation on corresponding bytes
    result = bytearray()
    for byte1, byte2 in zip(array1, array2):
        result.append(byte1 ^ byte2)

    return result

FLAG = open("./flag.txt", "rb").read()
RESU = open("./output.txt", "r").read()

hex_pairs = [RESU[i:i+2] for i in range(0, len(RESU), 2)]
# Convert each pair to a byte and create a bytearray
RESU_HEX = bytearray([int(pair, 16) for pair in hex_pairs])
# key = os.urandom(4) * 20

key4 = xor_byte_arrays(keep_only_n_bytes(RESU_HEX, 4), "FCSC".encode('utf-8'))
# check if working
resu4 = xor_byte_arrays(key4, keep_only_n_bytes(RESU_HEX, 4))

print("key4: ", key4)
print("RESU4: ", resu4)

key = key4 * 20
print("key: ", key)

key2 = keep_only_n_bytes(key, len(FLAG)+1)

print(len(key2))
print(len(RESU_HEX))
print("----------------------------")

RESU_XOR = xor_byte_arrays(RESU_HEX, key2)

print("RESU_XOR: ", RESU_XOR)