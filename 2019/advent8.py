#!/usr/bin/env python3

import sys
import math
import argparse
from collections import defaultdict

def print_usage(name):
    print("python3 {} <input file>".format(name))

def compute_image_crc(image_file, dim_x, dim_y):
    current_layer = 1
    current_pixel = 0
    pixels_per_layer = dim_x * dim_y

    layer_zeros = defaultdict(int)
    layer_ones = defaultdict(int)
    layer_twos = defaultdict(int)

    for line in image_file:
        print(f'line = {line}')
        image = line.strip()
        for index in range(len(image)):
            pixel = int(image[index])
            print(f'pixel = {pixel}')
            if pixel == 0:
                layer_zeros[current_layer] += 1
            if pixel == 1:
                layer_ones[current_layer] += 1
            if pixel == 2:
                layer_twos[current_layer] += 1

            current_pixel += 1
            if current_pixel % pixels_per_layer == 0:
                current_layer += 1

    min_zeros_layer = 0
    min_zeros = min(layer_zeros.values())
    for key, value in layer_zeros.items():
        if min_zeros == value:
            min_zeros_layer = key

    print(f'Total layers = {current_layer}')
    return layer_ones[min_zeros_layer] * layer_twos[min_zeros_layer]

def main():
    parser = argparse.ArgumentParser(description='Compute required fuel for modules, or modules+fuel')
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--x-dim', type=int)
    parser.add_argument('--y-dim', type=int)
    parser.add_argument('--modules-and-fuel', action='store_true', default=False, help='Compute fuel for modules plus the loaded fuel.')

    args = parser.parse_args()

    print(f'args = {args}')

    if (len(sys.argv) > 1):
        with args.file as input_file:
            image_crc = compute_image_crc(input_file, args.x_dim, args.y_dim)
            print(f'Min layer CRC = {image_crc}')
    else:
        print_usage(sys.argv[0])

if __name__ == "__main__":
    main()
