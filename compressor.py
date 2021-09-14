import pickle
import os

class Node:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right
        self.code = ''


"""
Array alpha stores characters in descending frequency
Array freq stores frequency of alpha in order

First take two characters of lowest frequency. Add two frequencies
If next least frequent char <= sum, node.left = char
Else build new tree and merge to main tree.
"""


def traverse_tree(node, val='', encoding=None):
    if encoding is None:
        encoding = {}
    newVal = val + str(node.code)
    if node.left:
        traverse_tree(node.left, newVal, encoding)
    if node.right:
        traverse_tree(node.right, newVal, encoding)
    if not (node.left or node.right):
        encoding[node.char] = newVal


def huffman_encoding(filename: str) -> dict:
    chars, freq = frequency_count(filename)
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

        left.code = 0
        right.code = 1

        # make new intermediate node
        newNode = Node(left.freq + right.freq, left.char + right.char, left,
                       right)

        # remove two smallest nodes
        nodes.remove(left)
        nodes.remove(right)

        # Add newNode
        nodes.append(newNode)

    encoding = {}
    traverse_tree(nodes[0], encoding=encoding)
    return encoding


def frequency_count(filename: str) -> tuple:
    """Returns a list of two lists which are the list of characters and their
    corresponding frequencies in filename, sorted by their frequencies.
    """
    file = open(filename, "r")
    text = file.read()
    char_dict = {}
    if text == '':
        return ([], [])
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
    return char_list, freq_list


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


def compress(filename: str, encoding) -> int:
    file = open(filename, "r")
    compressed_string = ""
    text = file.read()
    compressed_file = open("output/" + filename.split(".")[0] + "_compressed.txt", "wb")

    for index in range(len(text)):
        compressed_string += encoding[text[index]]

    compressed_file.write(str_to_byte(compressed_string))
    file.close()
    compressed_file.close()
    print("Compressed successfully")
    return len(compressed_string)


def compare_sizes(original: str) -> str:
    orig_size = os.path.getsize(original)
    compressed_size = os.path.getsize("output/" + original.split(".")[0] + "_compressed.txt")

    print("Size is compressed by " + "{:.1f}".format(((orig_size - compressed_size) * 100)/orig_size) + "%.")




if __name__ == "__main__":

    while 1:
        try:
            sample = input("What's the filename: ")
            if sample == "quit":
                print("Program terminated.")
                quit()
            f_encoding = huffman_encoding(sample)
            f_length = compress(sample, f_encoding)
            with open('output/data.pkl', 'wb') as f:
                pickle.dump(f_length, f)
                pickle.dump(f_encoding, f)

            compare_sizes(sample)

            quit()

        except FileNotFoundError:
            print("No such file.")







