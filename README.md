# Convert_raw
Repository to convert raw images to jpgs or pngs using Python 3.

### Dependencies: (python 3)
 - rawpy 
 - imageio 
 - tqdm

First, clone the xml_to_png.py script.

Next, install dependencies:
```
pip install -r requirements.txt
```

### Usage:
```
raw_to_png.py [-h] [--raw_dir RAW_DIR] [--save_dir SAVE_DIR]
                     [--ext EXT] [--save_ext SAVE_EXT]
                     
-h, --help           show this help message and exit
--raw_dir RAW_DIR    Directory with raw images.
--save_dir SAVE_DIR  Directory path to save converted images. (eg:
                     /home/user/converted_imgs)
--ext EXT            Image extension of the raw images (eg. 'raw').
--save_ext SAVE_EXT  Image file extension to convert to.
```
Example:
```
python raw_to_png.py --raw_dir /home/user/raw_pics --save_dir /home/user/converted_pics --ext raw --save_ext png
```


