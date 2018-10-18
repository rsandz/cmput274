# Write tree from path3.py into a file... then read it
import path3
import pickle

def write():
    tree = path3.tree_1()

    # Open File and Pickle the tree
    with open("pickle.out", "wb") as f:
        pickle.dump(tree, f)
        f.write(b"hello")

def read():
    with open("pickle.out", "rb") as f:
        tree = pickle.load(f)
        string = f.readline()

    print(tree, "".join([chr(i) for i in string]))

if __name__ == '__main__':
    print("Writing...")
    write()
    print("Done!\n")
    print("Reading...")
    read()