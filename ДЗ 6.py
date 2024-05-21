from heapq import heappush, heappop, heapify
import unittest


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(freq_dict):
    heap = [Node(char, freq) for char, freq in freq_dict.items()]
    heapify(heap)

    while len(heap) > 1:
        node1 = heappop(heap)
        node2 = heappop(heap)

        merged_node = Node(None, node1.freq + node2.freq)
        merged_node.left = node1
        merged_node.right = node2

        heappush(heap, merged_node)

    return heap[0]


def build_huffman_code_table(root):
    code_table = {}

    def build_code(node, code):
        if node.char is not None:
            code_table[node.char] = code
            return

        build_code(node.left, code + '0')
        build_code(node.right, code + '1')

    build_code(root, '')

    return code_table


def huffman_encoding(data):
    freq_dict = {}
    for char in data:
        freq_dict[char] = freq_dict.get(char, 0) + 1

    root = build_huffman_tree(freq_dict)
    code_table = build_huffman_code_table(root)

    encoded_data = ''.join(code_table[char] for char in data)

    return encoded_data, root


def huffman_decoding(encoded_data, root):
    decoded_data = ''

    node = root
    for bit in encoded_data:
        if bit == '0':
            node = node.left
        else:
            node = node.right

        if node.char is not None:
            decoded_data += node.char
            node = root

    return decoded_data


data = "Huffman coding is a method of lossless data compression"
encoded_data, root = huffman_encoding(data)
decoded_data = huffman_decoding(encoded_data, root)

print("Encoded data:", encoded_data)
print("Decoded data:", decoded_data)

