def find_encrypted_string(file_path, char):
    key = ord(char)
    # 打开并读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        hex_content = file.read()
        content = bytes.fromhex(hex_content)
        lines = content.splitlines()

    for line in lines:
        xor_result = ''.join([chr(s ^ key) for s in line])
        print(xor_result)


# 示例：假设文件路径为'text.txt'
file_path = 'p1_3_4_text.txt'
encrypted_characters = find_encrypted_string(file_path, 'x')

