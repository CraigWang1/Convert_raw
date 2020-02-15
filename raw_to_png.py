#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 21:03:45 2020

@author: craig
Script to take a directory of raw images and convert them into a new directory of converted jpg or png images.
"""

import rawpy, imageio, argparse, glob, os
from tqdm import tqdm

# Parse Arguments
def parse_args():
    parser = argparse.ArgumentParser(
        description="Put dataset in COCO format for machine learning training."
    )
    parser.add_argument(
        "--raw_dir",
        help="Directory with raw images.",
        type=str
    )
    parser.add_argument(
        "--save_dir",
        help="Directory path to save converted images. (eg: /home/user)",
        default="./",
        type=str
    )
    parser.add_argument(
        "--ext", help="Image extension of the raw images (eg. 'raw').", default="raw", type=str
    )
    parser.add_argument(
        "--save_ext", help="Image files extension to convert to.", default="png", type=str
    )
    
    args = parser.parse_args()
    # make the save directory if it doesn't exist
    if not os.path.isdir(args.save_dir):
        os.makedirs(args.save_dir)
        print("\nWarning: Your save directory was not an existing directory, so we created it.")
    return args

def convert(args):
    print('\n Converting raw .{} images to {}...'.format(args.ext, args.save_ext))
    raw_imgs = glob.glob(os.path.join(args.raw_dir, "*.{}".format(args.ext)))  #get all the raw images from the directory
    assert len(raw_imgs) > 0, 'No raw images found, perhaps the wrong raw file extension was inputted?'
    
    #iterate over all raw images to convert them 
    for fp in tqdm(raw_imgs):
        raw = rawpy.imread(fp)     #read the image
        rgb = raw.postprocess()    #process it
        base = os.path.splitext(os.path.basename(fp))[0]   #get the base filename (eg. 'test' from '/home/usr/test.png')
        new_fname = base + '.{}'.format(args.save_ext)     #add on our new extension (eg. 'test' -> 'test.png')
        imageio.imsave(os.path.join(args.save_dir, new_fname), rgb)  #save converted image to new directory
    #print empty line to look aesthetic
    print('')

if __name__ == '__main__':
    args = parse_args()
    convert(args)
