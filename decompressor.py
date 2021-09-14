import pickle


def decompress(compressed_file: str, encoding: dict, length: int) -> bool:
    file = open(compressed_file, "rb")
    decompressed_file = open("output/decompressed.txt", "w")
    compressed_text = file.read()
    compressed_str = ''
    for integer in compressed_text:
        compressed_str += format(integer, '08b')

    encoding_reversed = {val: key for key, val in encoding.items()}
    temp = ''
    text = ''
    i = 0
    while i < length:
        if temp not in encoding_reversed:
            temp += compressed_str[i]
            i += 1
        else:
            text += encoding_reversed[temp]
            temp = ''
    if temp in encoding_reversed:
        text += encoding_reversed[temp]

    decompressed_file.write(text)
    decompressed_file.close()
    file.close()
    return True


if __name__ == "__main__":

    f_path = "output/compressed.txt"

    with open('output/data.pkl', 'rb') as f:
        f_length = pickle.load(f)
        f_encoding = pickle.load(f)

    decompress(f_path, f_encoding, f_length)
