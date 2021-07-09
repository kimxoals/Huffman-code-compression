class Node:
    def __init__(self, freq=None, parent=None, char=None):
        self.freq = freq
        self.char = char
        self.parent = parent
        self.left = None
        self.right = None

class Main:
    """
    Array alpha stores characters in descending frequency
    Array freq stores frequency of alpha in order

    First take two characters of lowest frequency. Add two frequencies
    If next least frequent char <= sum, node.left = char
    Else build new tree and merge to main tree.
    """
    '''
    node_list = [get all node.val and find two smallest]

    Iterate through node_listL:
        find two nodes with smallest frequency
        combine and replace old two node with 1 new node
    '''


def frequency_count(filename: str) -> list:
    """Returns a list of two lists which are the list of characters and their
    corresponding frequencies in filename, sorted by their frequencies.
    """
    file = open(filename, "r")
    text = file.read()
    char_dict = {}
    if text == '':
        return [[],[]]
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


def compress(filename: str, prefix_dict: dict, bitlength: int) -> None:
    file = open(filename, "r")
    compressed_string = ""
    text = file.read()
    compressed_file = open("compressed.txt", "w")
    for index in range(len(text)):
        compressed_file.write(prefix_dict[text[index]])
    file.close()
    compressed_file.close()


if __name__ == "__main__":
    pass
    # new_dict = {'h' : "000", 'e' : "0015555555", 'l' : "010", 'o': "100"}
    # print(frequency_count("trial.txt"))
    # compress("trial.txt", new_dict, 3)

