cypher_text = bytes.fromhex(
    "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
).decode()


def xor_string_with_char(string, char):
    # 获取字母的ASCII码
    key = ord(char)

    # 对字符串的每个字符与字母的ASCII码进行异或操作
    xor_result = ''.join([chr(ord(s) ^ key) for s in string])

    return xor_result


# 示例使用
input_string = cypher_text
xor_char = 'X'  # 需要与'X'字母进行异或

result = xor_string_with_char(input_string, xor_char)
print("异或后的结果:", result)
