from Crypto.Util.Padding import pad, unpad

def pkcs7_pad(data: bytes, block_size: int) -> bytes:
    # 使用pad函数进行PKCS#7填充
    return pad(data, block_size)

def pkcs7_unpad(padded_data: bytes, block_size: int) -> bytes:
    # 使用unpad函数去除PKCS#7填充
    return unpad(padded_data, block_size)

# 示例
data = b"YELLOW SUBMARINE"
block_size = 20

# 进行填充
padded_data = pkcs7_pad(data, block_size)
print(f"填充后的数据: {padded_data}")

# 去除填充
unpadded_data = pkcs7_unpad(padded_data, block_size)
print(f"去除填充后的数据: {unpadded_data}")
