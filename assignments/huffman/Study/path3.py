import huffman

# Demonstrate making a tree

def tree_1():
    l_x = huffman.TreeLeaf(ord("x"))
    l_r = huffman.TreeLeaf(ord("r"))

    l_o = huffman.TreeLeaf(ord("o"))
    l_n = huffman.TreeLeaf(ord("n"))
    l_e = huffman.TreeLeaf(ord("e"))

    i_xr = huffman.TreeBranch(l_x,l_r)
    i_xre = huffman.TreeBranch(i_xr,l_e)

    i_on = huffman.TreeBranch(l_o,l_n)

    root = huffman.TreeBranch(i_on,i_xre)

    theTree = huffman.Tree([],root)

    ht_encoded = huffman.make_encoding_table(theTree.root)
    print(ht_encoded)

    # Write out theTree using pickle, NOT ht_encoded

    return(theTree)

if __name__ == '__main__':
    tree = tree_1()
    pass