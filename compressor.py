class Node:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right
        self.huff = ''


"""
Array alpha stores characters in descending frequency
Array freq stores frequency of alpha in order

First take two characters of lowest frequency. Add two frequencies
If next least frequent char <= sum, node.left = char
Else build new tree and merge to main tree.
"""


def printNodes(node, val='', char_dict=None):
    if char_dict is None:
        char_dict = {}
    newVal = val + str(node.huff)
    if node.left:
        printNodes(node.left, newVal, char_dict)
    if node.right:
        printNodes(node.right, newVal, char_dict)
    if not node.left and not node.right:
        char_dict[node.char] = newVal


def huffman_encoding(chars, freq) -> dict:
    nodes = []
    # initialize array of leaves
    for i in range(len(chars)):
        n = Node(freq[i], chars[i])
        nodes.append(n)

    while len(nodes) > 1:
        # Min heapify Nodes
        nodes = sorted(nodes, key=lambda x: x.freq)

        left = nodes[0]
        right = nodes[1]

        left.huff = 0
        right.huff = 1

        # make new intermediate node
        newNode = Node(left.freq + right.freq, left.char + right.char, left,
                       right)

        # remove two smallest nodes
        nodes.remove(left)
        nodes.remove(right)

        # Add newNode
        nodes.append(newNode)

    char_dict = {}
    printNodes(nodes[0], char_dict=char_dict)
    return char_dict


def frequency_count(filename: str) -> list:
    """Returns a list of two lists which are the list of characters and their
    corresponding frequencies in filename, sorted by their frequencies.
    """
    file = open(filename, "r")
    text = file.read()
    char_dict = {}
    if text == '':
        return [[], []]
    for index in range(len(text)):
        if text[index] not in char_dict:
            char_dict[text[index]] = 1
        else:
            char_dict[text[index]] += 1

    sorted_pair_list = sorted(char_dict.items(), key=lambda pair: pair[1])
    freq_list = []
    char_list = []

    for item in sorted_pair_list:
        freq_list.append(item[1])
        char_list.append(item[0])
    return [char_list, freq_list]


def str_to_byte(bit_str: str) -> bytes:
    byte_array = bytearray()
    q, r = divmod(len(bit_str), 8)
    for index in range(0, q * 8, 8):
        byte_array.append(int(bit_str[index: index + 8], 2))
    if r != 0:
        remainder = bit_str[q * 8:]
        remainder += '0' * (8 - r)
        byte_array.append(int(remainder, 2))
    return bytes(byte_array)


def compress(filename: str) -> list:
    file = open(filename, "r")
    compressed_string = ""
    text = file.read()
    compressed_file = open("output/compressed.txt", "wb")
    char_freq = frequency_count(filename)
    prefix_dict = huffman_encoding(char_freq[0], char_freq[1])

    for index in range(len(text)):
        compressed_string += prefix_dict[text[index]]

    compressed_file.write(str_to_byte(compressed_string))
    file.close()
    compressed_file.close()
    return [len(compressed_string), prefix_dict]


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


if __name__ == "__main__":

    dictio = compress("lorem.txt")
    decompress("output/compressed.txt", dictio)
