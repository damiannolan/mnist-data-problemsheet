# Adapted from:  https://stackoverflow.com/questions/2872381/how-to-read-a-file-byte-by-byte-in-python-and-how-to-print-a-bytelist-as-a-binar

import gzip
import numpy as np
import PIL.Image as pil

def read_labels_from_file(filename):
    with gzip.open(filename, 'rb') as f:
        # Get the magic number
        magic = f.read(4)
        magic = int.from_bytes(magic, 'big')
        print("Magic is: ", magic)

        # Get the number of labels
        nolab = f.read(4)
        nolab = int.from_bytes(nolab, 'big')
        print("Number of labels: ", nolab)

        # Read the labels into an appropriate data structure i.e as array
        labels = [f.read(1) for i in range(nolab)]
        labels = [int.from_bytes(label, 'big') for label in labels]

        return labels

train_labels = read_labels_from_file('data/train-labels-idx1-ubyte.gz')
test_labels = read_labels_from_file('data/t10k-labels-idx1-ubyte.gz')

# A function to read the images
def read_images_from_file(filename):
    with gzip.open(filename, 'rb') as f:
        # Get the magic number
        magic = f.read(4)
        magic = int.from_bytes(magic, 'big')
        print("Magic is: ", magic)

        # Get the number of images
        noimages = f.read(4)
        noimages = int.from_bytes(noimages, 'big')
        print("Number of images: ", noimages)

        # Number of rows
        norows = f.read(4)
        norows = int.from_bytes(norows, 'big')
        print("Rows: ", norows)

        # Number of columns
        nocols = f.read(4)
        nocols = int.from_bytes(nocols, 'big')
        print("Columns: ", nocols)

        images = []

        for i in range(noimages):
            rows = []
            for j in range(norows):
                cols = []
                for k in range(nocols):
                    cols.append(int.from_bytes(f.read(1), 'big'))
                rows.append(cols)
            images.append(rows)

        return images

train_images = read_images_from_file('data/train-images-idx3-ubyte.gz')

for row in train_images[4999]:
    for col in row:
        print('.' if col < 128 else '#', end='')
    print()

img = train_images[4999]
img = np.array(img)
img = pil.fromarray(img.astype('uint8'))
img = img.convert('RGB')
img.show()
img.save('2.png')

