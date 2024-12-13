import base64


def hex_to_base64(hex_str):
    # 将hex字符串转换为字节
    bytes_data = bytes.fromhex(hex_str)
    # 将字节数据转换为Base64编码
    base64_str = base64.b64encode(bytes_data)
    # 返回Base64编码并解码为字符串
    return base64_str.decode('utf-8')


# 示例使用
hex_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"  # 这是 "Hello World" 的hex表示
base64_str = hex_to_base64(hex_str)
print("Base64编码:", base64_str)
