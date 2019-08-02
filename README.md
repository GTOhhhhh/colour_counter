# Colour Counter
A simple app which lets the user upload a PNG image file, converts it to a greyscale image with a 256 colorspace then
counts the number of coloured areas.

**Try uploading some test images from the `test_files` directory through the app and view the output.**

Additionally, the `count_areas.py` service may be ran as a standalone script to process an array of unsigned 256 
integers as explained below.

# Installing
Requires Linux/OSX and Python 3.5 or higher. 

If you wish to use virtualenv (`pip3 install virtualenv`) then you may use the included script `setup.sh` to automatically activate a new virtualenv, install requirements and run the app. By doing:
1. `chmod +x setup.sh`
2. `./setup.sh`

Otherwise:

1. Install dependencies (`pip3 install .`)
2. Run (`python3 app.py`)
3. Open [http://localhost:5000](http://localhost:5000)

To run `count_areas.py` as a command line script:

1. `cd services` from the root directory
2. `chmod +x count_areas.py`
3. Run `count_areas.py <input-filename> --shape <height>,<width>` - e.g. `./count_areas.py sample.bin --shape 256,256`

or simply:
1. `cd services` from the root directory
2. `python3 count_areas.py <input-filename> --shape <height>,<width>` - e.g `python3 count_areas.py sample.bin --shape 256,256`

# Reference material for algorithm design
- https://www.sciencedirect.com/science/article/pii/S0031320317301693
- https://blogs.mathworks.com/steve/2007/03/06/connected-component-labeling-part-1/?s_tid=blogs_rc_2
- https://pdfs.semanticscholar.org/8bfd/42a8eb013667bb8a0082c215d6f2db62776a.pdf
