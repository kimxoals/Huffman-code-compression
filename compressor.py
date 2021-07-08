class Node:
    def __init__(self, val=None, parent=None):
        self.val = val
        self.parent = parent
        self.left = None
        self.right = None


class Leaf:
    def __init__(self, char, freq):
        self.parent = None
        self.char = char
        self.freq = freq


class Main:
    """
    Array alpha stores characters in descending frequency
    Array freq stores frequency of alpha in order

    First take two characters of lowest frequency. Add two frequencies
    If next least frequent char <= sum, node.left = char
    Else build new tree and merge to main tree.
    """

    # char = {'a':10, 'e':15, 'i':12,'s':3,'t':4,'p':13,'\n':1}
    # sort dictionary on ascending value
    # char = {k: v for k, v in sorted(char.items(), key=lambda item: item[1])}

    alpha = ['\n', 's', 't', 'a', 'i', 'p', 'e']
    freq = [1, 3, 4, 10, 12, 13, 15]

    l_space = Leaf(alpha[0], freq[0])
    l_s = Leaf(alpha[1], freq[1])

    n1 = Node(l_space.freq + l_s.freq)
    n1.left = l_space
    n1.right = l_s

    l_t = Leaf(alpha[2], freq[2])

    if l_t.freq <= n1.val:
        n2 = Node(l_t.freq + n1.val)
        n1.parent = n2
        n2.left = l_t
        n2.right = n1

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
