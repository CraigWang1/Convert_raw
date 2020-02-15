# Convert_raw
Repository with code to convert raw images to jpgs or pngs using Python 3.

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
                     /home/user)
--ext EXT            Image extension of the raw images (eg. 'raw').
--save_ext SAVE_EXT  Image files extension to convert to.
```


