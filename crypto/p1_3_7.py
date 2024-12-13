import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64


def read_file(file_path='p1_3_7_text.txt'):
    with open(file_path, 'r', encoding='utf-8') as file:
        cipher_base64 = file.read()
        cipher = base64.b64decode(cipher_base64)
        return cipher


def decrypt_aes_ecb(ciphertext, key):
    # 创建AES解密器，模式为ECB
    cipher = AES.new(key, AES.MODE_ECB)

    # 解密数据并移除填充
    decrypted_data = cipher.decrypt(ciphertext)
    try:
        # 如果使用了PKCS7填充，使用unpad移除填充
        decrypted_data = unpad(decrypted_data, AES.block_size)
    except ValueError:
        pass  # 如果没有填充，忽略这个错误

    return decrypted_data


# 示例使用
# Base64 编码的加密文本
key = 'YELLOW SUBMARINE'.encode()

# 将加密文本从Base64解码为字节
ciphertext = read_file()

# 解密
decrypted_text = decrypt_aes_ecb(ciphertext, key)

# 将字节解码为字符串
print(f"解密后的文本: {decrypted_text.decode('utf-8')}")
