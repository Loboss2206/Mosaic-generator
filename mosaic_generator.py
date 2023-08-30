#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt
import skimage.io as skio
from skimage.transform import resize

def load_image(filepath):
    return skio.imread(filepath)

def load_patch_images(patch_dir):
    patch_images = []
    for filename in os.listdir(patch_dir):
        if os.path.isfile(os.path.join(patch_dir, filename)):
            patch_images.append(skio.imread(os.path.join(patch_dir, filename)))
    return patch_images

def calculate_mean_patch_colors(patch_images):
    mean_colors = []
    for img in patch_images:
        mean_color = np.mean(img, axis=(0, 1))
        mean_colors.append(mean_color)
    return np.array(mean_colors) / 255.0

def create_mosaic(image, block_size, patches, mean_patch_colors):
    rows, cols = image.shape[0] // block_size, image.shape[1] // block_size
    mosaic = np.zeros((rows * block_size, cols * block_size, 3))
    
    for i in range(rows):
        for j in range(cols):
            block = image[i * block_size:(i + 1) * block_size, j * block_size:(j + 1) * block_size]
            block_color = np.mean(block, axis=(0, 1)) / 255.0
            color_diffs = np.sum(np.abs(mean_patch_colors - block_color), axis=1)
            best_patch_idx = np.argmin(color_diffs)
            
            mosaic[i * block_size:(i + 1) * block_size, j * block_size:(j + 1) * block_size] = \
                resize(patches[best_patch_idx], (block_size, block_size))
    
    return (mosaic * 255).astype(int)

if __name__ == '__main__':
    main_image_name = 'kira.jpg'
    patch_directory = './patches'
    block_size = 16

    main_image = load_image(main_image_name)
    patch_images = load_patch_images(patch_directory)
    mean_patch_colors = calculate_mean_patch_colors(patch_images)
    
    mosaic_image = create_mosaic(main_image, block_size, patch_images, mean_patch_colors)
    
    plt.figure()
    plt.imshow(mosaic_image)
    plt.title(f"Mosaic image with block size: {block_size}x{block_size}")
    plt.show()
