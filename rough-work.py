# Adapted from
# https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python
# https://stackoverflow.com/questions/2872381/how-to-read-a-file-byte-by-byte-in-python-and-how-to-print-a-bytelist-as-a-binar

import gzip
import numpy as np

f = gzip.open('data/train-images-idx3-ubyte.gz', 'rb')

# firstbyte = f.read(1)
# print(firstbyte)

magicNumber = f.read(4)
print(magicNumber)

print(int.from_bytes(magicNumber, byteorder='big'))

print(int.from_bytes(f.read(4), byteorder='big'))
print(int.from_bytes(f.read(4), byteorder='big'))
print(int.from_bytes(f.read(4), byteorder='big'))

image = [[0 for x in range(28)] for y in range(28)]


for i in range(28):
    for j in range(28):
        image[i][j] = int.from_bytes(f.read(1), byteorder='big')

for i in range(28):
    for j in range(28):
        if image[i][j] < 128:
            print(".", end="")
        else:
            print("#", end="")

       # print(image[i][j], end="")
    print()

for i in range(28):
    for j in range(28):
        image[i][j] = int.from_bytes(f.read(1), byteorder='big')

for i in range(28):
    for j in range(28):
        if image[i][j] < 128:
            print(".", end="")
        else:
            print("#", end="")

    print()

for i in range(28):
    for j in range(28):
        image[i][j] = int.from_bytes(f.read(1), byteorder='big')

for i in range(28):
    for j in range(28):
        if image[i][j] < 128:
            print(".", end="")
        else:
            print("#", end="")
    print()
f.close()

def save_image(image, label, directory):

    output = "images/%s-%05d-%d"
    print(output % (directory, image, label))

save_image(1, 5, "train")

img = train_images[4999]
img = np.array(img)
img = pil.fromarray(img.astype('uint8'))
img = img.convert('RGB')
img.show()
img.save('2.png')
