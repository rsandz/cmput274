# ====================
# Make a tree directly
# ====================
#
# October 9

import huffman

def tree_1():
    """
    Makes my own custom Tree!!!
    """

    # Lets make some leaf nodes!
    # ==========================
    l_x = huffman.TreeLeaf(ord("x"))
    l_r = huffman.TreeLeaf(ord("r"))
    
    l_o = huffman.TreeLeaf(ord("o"))
    l_n = huffman.TreeLeaf(ord("n"))

    l_e = huffman.TreeLeaf(ord("e"))

    # Lets make the interior nodes!
    # =============================

    # Lowest level of tree
    n_01 = huffman.TreeBranch(l_x, l_r)

    # 2nd Level of the Tree
    n_11 = huffman.TreeBranch(l_o, l_n)
    n_12 = huffman.TreeBranch(n_01, l_e)

    # Root Node
    root = huffman.TreeBranch(n_11, n_12)

    nodes = [n_01, n_11, n_12, root]

    # Lets make the tree!
    # ===================
    return huffman.Tree(nodes, root)


if __name__ == "__main__":
    # Run when in called from CLI
    myTree = tree_1()
    