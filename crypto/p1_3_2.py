def xor_buffers(buffer1, buffer2):
    # Ensure both buffers have the same length
    if len(buffer1) != len(buffer2):
        raise ValueError("Buffers must have the same length")

    # Perform XOR operation between each pair of bytes
    return bytes([b1 ^ b2 for b1, b2 in zip(buffer1, buffer2)])


# Example usage
buffer1 = bytes.fromhex("1c0111001f010100061a024b53535009181c")
buffer2 = bytes.fromhex("686974207468652062756c6c277320657965")

result = xor_buffers(buffer1, buffer2)
print("XOR result:", result.hex())  # Output result in hex format
