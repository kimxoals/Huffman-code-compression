import pprint


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
        # print(repr(f"{node.char} -> {newVal}"))


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

        # print([(node.char, node.freq) for node in nodes])
    char_dict = {}
    printNodes(nodes[0], char_dict=char_dict)
    pprint.pprint(char_dict)
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
    for index in range(0, len(bit_str), 8):
        byte_array.append(int(bit_str[index : index + 8], 2))
    return bytes(byte_array)


def compress(filename: str) -> None:
    file = open(filename, "r")
    compressed_string = ""
    text = file.read()
    compressed_file = open("compressed.txt", "wb")
    char_freq = frequency_count(filename)
    prefix_dict = huffman_encoding(char_freq[0], char_freq[1])

    for index in range(len(text)):
        compressed_string += prefix_dict[text[index]]

    compressed_file.write(str_to_byte(compressed_string))
    file.close()
    compressed_file.close()


def decompress(compressed_file: str) -> str:
    pass


if __name__ == "__main__":
    chars = ['e', 'a', 'd', 'b', 'c', '\n']
    freq = [2, 3, 4, 5, 6, 10]

    # lookup_dict = huffman_encoding(chars, freq)


    # print(lookup_dict)
    # compress(dict)
    # new_dict = {'h' : "000", 'e' : "001", 'l' : "010", 'o': "100"}
    # print(frequency_count("trial.txt"))
    compress("lorem.txt")
