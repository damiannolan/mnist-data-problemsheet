# MNIST Data Set

## Emerging Technologies - Problem Sheet 2

This repository contains solutions to a series of problems relating to the famous MNIST data set. The data sets are in a
bespoke format and can be obtained from the website found [HERE!](http://yann.lecun.com/exdb/mnist/)

The repository contains a basic python script which uses a series of functions written to decompress and read the .gz files.

The functions are listed as follows:

- read_labels_from_file
- read_images_from_file
- save_image
- print_image

The original problem sheet can be found [HERE!](https://emerging-technologies.github.io/problems/mnist.html)


## 1. Read the data files
Download the image and label files.
Have Python decompress and read them byte by byte into appropriate data structures in memory.

## 2. Output an image to the console
Output the third image in the training set to the console.
Do this by representing any pixel value less than 128 as a full stop and any other pixel value as a hash symbol.

## 3. Output the image files as PNGs
Use Python to output the image files as PNGs, saving them in a subfolder in your repository.
Name the images in the format `train-XXXXX-Y.png` or `test-XXXXX-Y.png` where `XXXXX` is the image number (where it
occurs in the data file) and `Y` is its label.
For instance, the five-thousandth training image is labelled 2, so its file name should be `train-04999-2.png`.
Note the images are indexed from 0, so the five-thousandth image is indexed as 4999.
