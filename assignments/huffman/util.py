import bitio
import huffman
import pickle
import sys


def read_tree(tree_stream):
    '''Read a description of a Huffman tree from the given compressed
    tree stream, and use the pickle module to construct the tree object.
    Then, return the root node of the tree itself.

    Args:
      tree_stream: The compressed stream o read the tree from.

    Returns:
      A Huffman tree root constructed according to the given description.
    '''
    
    # Unserialize and return the node
    tree_root = pickle.load(tree_stream)
    return tree_root


def decode_byte(tree, bitreader):
    """
    Reads bits from the bit reader and traverses the tree from
    the root to a leaf. Once a leaf is reached, bits are no longer read
    and the value of that leaf is returned.

    EOF Error is raised when bitreader has reached EOF
    Args:
      bitreader: An instance of bitio.BitReader to read the tree from.
      tree: A Huffman tree.

    Returns:
      Next byte of the compressed bit stream.
    """
    # Read from bitreader until done
    current_node = tree.root
    
    while True:
        try:
            bit = int(bitreader.readbit())
        except EOFError:
            raise RuntimeError("Partial Encoding/Bits in compressed file")

        if bit == 0:
            current_node = current_node.left
        elif bit == 1:
            current_node = current_node.right
        else:
            raise TypeError("Bitreader returned non-binary")

        # Check if done
        if isinstance(current_node, huffman.TreeLeaf):
            return current_node.value
    
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
    # Init
    tree = read_tree(compressed)
    comp_reader = bitio.BitReader(compressed)
    uncomp_writer = bitio.BitWriter(uncompressed)
    
    # Uncompress the compressed stream
    while True:
        uncomp_byte = decode_byte(tree, comp_reader)

        # Check if EOF marker
        if uncomp_byte is None:
            break

        uncomp_writer.writebits(uncomp_byte, 8)

    # Flush and then we're done
    uncomp_writer.flush()
    
    
def write_tree(tree, tree_stream):
    '''Write the specified Huffman tree to the given tree_stream
    using pickle.

    Args:
      tree: A Huffman tree.
      tree_stream: The binary file to write the tree to.
    '''
    pickle.dump(tree, tree_stream)


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
    '''
    # Init
    write_tree(tree, compressed)
    encoding_table = huffman.make_encoding_table(tree.root)

    comp_writer = bitio.BitWriter(compressed)
    uncomp_reader = bitio.BitReader(uncompressed)

    try:
        while True:
            byte = uncomp_reader.readbits(8)
            to_write = encoding_table[byte]

            # The above is in a format of True or False
            for bool in to_write:
                comp_writer.writebit(bool)
    
    except EOFError:
        # Flush and we're done
        comp_writer.flush()
