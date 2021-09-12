def decompress(compressed_file: str, len_n_prefix: list) -> str:
    file = open(compressed_file, "rb")
    decompressed_file = open("output/decompressed.txt", "w")
    compressed_text = file.read()
    compressed_str = ''
    for integer in compressed_text:
        compressed_str += format(integer, '08b')

    inv_prefix = {v: k for k, v in len_n_prefix[1].items()}
    temp = ''
    text = ''
    i = 0
    while i < len_n_prefix[0]:
        if temp not in inv_prefix:
            temp += compressed_str[i]
            i += 1
        else:
            text += inv_prefix[temp]
            temp = ''
    if temp in inv_prefix:
        text += inv_prefix[temp]

    decompressed_file.write(text)
    decompressed_file.close()
    file.close()
    return "success"
