import bitio
import huffman
import pickle


def read_tree(tree_stream):
    '''Read a description of a Huffman tree from the given compressed
    tree stream, and use the pickle module to construct the tree object.
    Then, return the root node of the tree itself.

    Args:
      tree_stream: The compressed stream o read the tree from.

    Returns:
      A Huffman tree root constructed according to the given description.
    '''
    # Get the entire tree's binary representation
    tree_byte_array = bytearray()
    while True:
        try:
            tree_byte_array += tree_stream.readbits(tree_stream)
        except EOFError:
            break

    # Unserialize and return the node
    tree_root = pickle.loads(tree_byte_array)
    return tree_root


def decode_byte(tree, bitreader):
    """
    Reads bits from the bit reader and traverses the tree from
    the root to a leaf. Once a leaf is reached, bits are no longer read
    and the value of that leaf is returned.

    Args:
      bitreader: An instance of bitio.BitReader to read the tree from.
      tree: A Huffman tree.

    Returns:
      Next byte of the compressed bit stream.
    """
    # Read from bitreader until done
    currentNode = tree.root
    while True:
        bit = bitreader.readbit()
        if bit == 0:
            currentNode = currentNode.left
        elif bit == 1:
            currentNode = currentNode.right
        else:
            raise TypeError("Bitreader returned non-binary")

        # Check if done
        if isinstance(currentNode, huffman.TreeLeaf):
            return currentNode.value
    
    # TODO: Check for if byte not in tree


def decompress(compressed, uncompressed):
    '''First, read a Huffman tree from the 'tree_stream' using your
    read_tree function. Then use that tree to decode the rest of the
    stream and write the resulting symbols to the 'uncompressed'
    stream.

    Args:
      compressed: A file stream from which compressed input is read.
      uncompressed: A writable file stream to which the uncompressed
          output is written.
    '''
    


def write_tree(tree, tree_stream):
    '''Write the specified Huffman tree to the given tree_stream
    using pickle.

    Args:
      tree: A Huffman tree.
      tree_stream: The binary file to write the tree to.
    '''
    pass


def compress(tree, uncompressed, compressed):
    '''First write the given tree to the stream 'tree_stream' using the
    write_tree function. Then use the same tree to encode the data
    from the input stream 'uncompressed' and write it to 'compressed'.
    If there are any partially-written bytes remaining at the end,
    write 0 bits to form a complete byte.

    Flush the bitwriter after writing the entire compressed file.

    Args:
      @param tree: A Huffman tree.
      uncompressed: A file stream from which you can read the input.
      compressed: A file stream that will receive the tree description
          and the coded input data.
      tree_stream: A file stream where the tree data should be dumped.
    '''
    pass
