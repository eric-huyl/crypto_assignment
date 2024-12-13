import base64


def read_file(file_path='p1_3_6_text.txt'):
    with open(file_path, 'r', encoding='utf-8') as file:
        crypted_base64 = file.read()
        crypted = base64.b64decode(crypted_base64)
        return crypted


def hamming_distance(bytes1, bytes2):
    distance = 0
    for ch1, ch2 in zip(bytes1, bytes2):
        # 将字符转为ASCII码并进行异或运算
        xor_result = ch1 ^ ch2
        # 计算异或结果中1的个数，即不同的位的个数
        distance += bin(xor_result).count('1')
    return distance


def find_key_size():
    crypted = read_file()
    for key_size in range(2, 20):
        bytes1 = crypted[0:key_size]
        bytes2 = crypted[key_size + 1:2 * key_size + 1]
        distance = hamming_distance(bytes1, bytes2)
        print(f'SIZE:{key_size} DIS:{distance}')


def get_new_blocks():
    crypted = read_file()
    new_blocks = [[], [], [], []]
    index = 0
    for byte in crypted:
        new_blocks[index].append(byte)
        index = (index + 1) % 4

    return new_blocks


def break_single_xor(input=[], char='X'):
    key = ord(char)
    byte_arr = bytearray(input)
    bytes_obj = bytes(byte_arr)
    xor_result = ''.join([chr(s ^ key) for s in bytes_obj])
    print(xor_result)

new_blocks = get_new_blocks()
break_single_xor(new_blocks[0], 'u')
