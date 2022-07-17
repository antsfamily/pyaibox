"""


class HuffmanCoding: def __init__(self, path):
                         ...

    def __init__(self, path):
        ...

    class HeapNode: def __init__(self, char, freq):
                        ...

        def __init__(self, char, freq):
            ...

        def __lt__(self, other):
            ...

        def __eq__(self, other):
            ...

    def make_frequency_dict(self, text):
        ...

    def make_heap(self, frequency):
        ...

    def merge_nodes(self):
        ...

    def make_codes_helper(self, root, current_code):
        ...

    def make_codes(self):
        ...

    def get_encoded_text(self, text):
        ...

    def pad_encoded_text(self, encoded_text):
        ...

    def get_byte_array(self, padded_encoded_text):
        ...

    def compress(self, outfile=None):
    """ functions for decompression: """

    def remove_padding(self, padded_encoded_text):
        ...

    def decode_text(self, encoded_text):
        ...

    def decompress(self, infile, outfile=None):

