import struct
import numpy as np


def read_flo(file_path):
    with open(file_path, 'rb') as file:
        print(file.read(4))
        width, height = struct.unpack('<LL', file.read(8))
        vectors = np.fromfile(file, dtype='uint32', count=-1, sep="")
        vectors = vectors.reshape((height, width, 2), order='A')

        return width, height, vectors
