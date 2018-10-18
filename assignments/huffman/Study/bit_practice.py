# BITIO Worksheet
import bitio

def oneBitReader():
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

def multiBitReader():
    with open("sample.txt", "rb") as f:
        out = ""
        charOut = ""
        bitReader = bitio.BitReader(f)
        try:
            while True:
                byte = bitReader.readbits(8)
                out += str(byte) + " "
                charOut += chr(byte)

        except EOFError:
            pass

        print(out)
        print(charOut)

def bitWriter(msg = "01110011011101000111010101100100011110010010000001101000011000010111001001100100"):
    with open("message.txt", "wb") as f:
        bitWriter = bitio.BitWriter(f)
        for bit in msg:
            bitWriter.writebit(int(bit))
        
        bitWriter.flush()

def multiBitWriter():
    msg = [87, 101, 32, 97, 114, 101, 32, 116, 104, 101, 32, 66, 111, 114, 103, 46,
            10, 82, 101, 115, 105, 115, 116, 97, 110, 99, 101, 32, 105, 115, 32,
            102, 117, 116, 105, 108, 101, 33, 10]
    with open("message.txt", "wb") as f:
        bitWriter = bitio.BitWriter(f)
        for byte in msg:
            bitWriter.writebits(byte, 8)

        bitWriter.flush()
        f.flush()
    
if __name__ == "__main__":
    #bitWriter("011010000110010101101100011011000110111")
    multiBitWriter()
