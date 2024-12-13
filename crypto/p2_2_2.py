def cbc_decrypt(ciphertext: bytes, key: bytes, iv: bytes) -> bytes:
    block_size = len(key)
    plaintext = b''
    previous_block = iv

    # 分块解密
    for i in range(0, len(ciphertext), block_size):
        block = ciphertext[i:i + block_size]

        # 解密块
        decrypted_block = xor_bytes(block, key)

        # 与前一个密文块或IV异或
        plaintext_block = xor_bytes(decrypted_block, previous_block)

        # 更新链式依赖
        plaintext += plaintext_block
        previous_block = block

    return plaintext


def xor_bytes(a: bytes, b: bytes) -> bytes:
    return bytes(i ^ j for i, j in zip(a, b))


def cbc_encrypt(plaintext: bytes, key: bytes, iv: bytes) -> bytes:
    block_size = len(key)  # 假设 key 的长度等于块大小
    ciphertext = b''
    previous_block = iv

    # 分块加密
    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i + block_size]

        # 填充块，如果不足block_size
        if len(block) < block_size:
            padding_length = block_size - len(block)
            block += bytes([padding_length] * padding_length)

        # 与前一个密文块或IV异或
        block_to_encrypt = xor_bytes(block, previous_block)

        # 使用密钥（这里使用XOR来模拟加密算法）
        encrypted_block = xor_bytes(block_to_encrypt, key)

        # 更新链式依赖
        ciphertext += encrypted_block
        previous_block = encrypted_block

    return ciphertext


# 示例数据
key = b'sixteen byte key'  # 密钥，长度必须与块大小相同
iv = b'sixteen byte iv '  # 初始向量，长度必须与块大小相同
plaintext = b'Hello, CBC Mode!'  # 明文

# 加密
ciphertext = cbc_encrypt(plaintext, key, iv)
print(f"加密后的密文: {ciphertext}")

# 解密
decrypted_text = cbc_decrypt(ciphertext, key, iv)
print(f"解密后的明文: {decrypted_text}")
