# BITIO Worksheet
import bitio

with open("sample.txt", "rb") as f:
    out = ""
    bitReader = bitio.BitReader(f)
    acc = 1
    try:
        while True:
            bit = bitReader.readbit()
            out += str(bit)

            if acc == 8:
                acc = 0 
                out += " "
            acc += 1
    except EOFError:
        pass

    print(out)