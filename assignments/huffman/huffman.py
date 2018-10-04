from collections import Counter

class Tree:
    """
    Stores the Huffman tree itself as a collection of nodes,
    for pickling. 

    The root of the tree is redefined for easy access to the start
    of the tree.
    """
    pass

class TreeLeaf:
    """
    Leaf node of a Huffman tree. Stores the value.

    Should store an 8-bit integer to represent a single byte, or None
    to indicate the special "end of message" character.
    """
    pass

class TreeBranch:
    """
    Simple representation of an internal node on a Huffman tree.
    Just stores the two children.
    """
    pass

def custom_min(trees):
    """ Takes a list of tuples called trees, finds the smallest 
    item and removes it from the list. Both the smallest item and
    new list are returned.

    Each item in trees is a tuple of (symbol, frequency)
    """
    pass



def make_tree(freq_table):
    """
    Constructs and returns the Huffman tree from the given frequency table.
    """
    pass

def make_encoding_table(huffman_tree):
    """
    Given a Huffman tree, will make the encoding table mapping each
    byte (leaf node) to its corresponding bit sequence in the tree.
    """
    pass


def make_freq_table(stream):
    """
    Given an input stream, will construct a frequency table
    (i.e. mapping of each byte to the number of times it occurs in the stream).

    The frequency table is actually a dictionary.
    """
    freq_dict = {}
    buffer = bytearray(512)

    # Read from the file
    while True:
        count = stream.readinto(buffer)

        # Count Bytes
        for index, b in enumerate(buffer):
            # Check if we reached EOF
            if index >= count:
                break

            if b not in freq_dict:
                freq_dict[b] = 1
            else:
                freq_dict[b] += 1
        
        # End of Stream
        if count < len(buffer):
            break
            
    return freq_dict


# Testing Code

TEST = True

if __name__ == "__main__" and TEST:
    f = open("test.in", "r+b")
    ft = make_freq_table(f)
    print(ft)
    print(sum(ft.values()))
    pass