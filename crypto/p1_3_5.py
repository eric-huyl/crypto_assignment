def repeating_key_xor(plaintext, key):
    ciphertext = []
    key_length = len(key)

    for i, char in enumerate(plaintext):
        # 找到当前密钥中的字符
        current_key_char = key[i % key_length]

        # 对明文字符和当前密钥字符进行 XOR 运算
        xor_char = ord(char) ^ ord(current_key_char)

        # 将 XOR 结果转为十六进制，并添加到结果列表
        ciphertext.append(format(xor_char, '02x'))

    # 将所有的十六进制字符连接成最终密文
    return ''.join(ciphertext)


# 示例使用
plaintext = "Burning 'em, if you ain't quick and nimble"
key = "ICE"
ciphertext = repeating_key_xor(plaintext, key)
print("Ciphertext (hex):", ciphertext)
